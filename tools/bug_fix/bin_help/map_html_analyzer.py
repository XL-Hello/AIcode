#!/usr/bin/env python3
"""
Map文件HTML分析器
基于segment_analyzer.py，生成HTML格式的分析报告
功能：1. 显示所有段的总览 2. 生成树状结构查看目录的占用和占比
"""

import re
import sys
import argparse
import json
from pathlib import Path
from collections import defaultdict
from datetime import datetime


class MapHtmlAnalyzer:
    def __init__(self, include_debug=False, max_dir_levels=10):
        self.segments = {}  # {segment_name: {'start_addr': addr, 'size': size, 'files': {filename: size}, 'directories': {dirname: {'size': size, 'file_count': count}}}}
        self.include_debug = include_debug
        self.max_dir_levels = max_dir_levels
        self.file_to_directories = {}  # {segment_name: {filename: [dir_paths]}} 文件到目录的映射
        
    def parse_map_file(self, map_file_path):
        """解析map文件"""
        try:
            with open(map_file_path, 'r', encoding='utf-8') as f:
                content = f.read()
        except Exception as e:
            print(f"读取文件失败: {e}")
            return False
            
        # 解析段定义
        self._parse_segment_definitions(content)
        
        # 解析各个段内的符号和文件占用
        self._parse_segment_details(content)
        
        return True
    
    def _parse_segment_definitions(self, content):
        """解析段定义"""
        # 匹配段定义行，格式如: .psram_text     0x0000000034300000   0x481000
        pattern = r'^(\.[\w_]+)\s+0x([0-9a-fA-F]+)\s+0x([0-9a-fA-F]+)'
        
        for match in re.finditer(pattern, content, re.MULTILINE):
            segment_name = match.group(1)
            start_addr = int(match.group(2), 16)
            size = int(match.group(3), 16)
            
            # 检查是否是debug段
            if not self.include_debug and self._is_debug_segment(segment_name):
                continue
            
            self.segments[segment_name] = {
                'start_addr': start_addr,
                'size': size,
                'files': defaultdict(int),
                'directories': defaultdict(lambda: {'size': 0, 'file_count': 0})
            }
            self.file_to_directories[segment_name] = defaultdict(list)
    
    def _is_debug_segment(self, segment_name):
        """检查是否是debug相关段"""
        debug_segments = ['.debug_', '.comment', '.note.', '.eh_frame', '.stab']
        return any(segment_name.startswith(debug) for debug in debug_segments)
    
    def _parse_segment_details(self, content):
        """解析各段内的符号和文件占用"""
        lines = content.split('\n')
        current_segment = None
        symbols_found = 0
        
        for i, line in enumerate(lines):
            # 检查是否是段定义开始
            segment_match = re.match(r'^(\.[\w_]+)\s+0x[0-9a-fA-F]+\s+0x[0-9a-fA-F]+', line)
            if segment_match:
                segment_name = segment_match.group(1)
                if segment_name in self.segments:
                    current_segment = segment_name
                continue
            
            # 检查是否是段结束标记
            if current_segment and re.search(rf'__{current_segment[1:]}_end\s*=', line):
                current_segment = None
                continue
            
            # 如果在段内，解析符号占用
            if current_segment:
                if self._parse_symbol_in_segment(line, current_segment):
                    symbols_found += 1
    
    def _parse_symbol_in_segment(self, line, segment_name):
        """解析段内的符号信息"""
        # 匹配单行格式
        pattern1 = r'^\s+(\.[\w.]+)\s+0x[0-9a-fA-F]+\s+0x([1-9a-fA-F][0-9a-fA-F]*)\s+(.*)$'
        match1 = re.match(pattern1, line)
        if match1:
            symbol_name = match1.group(1)
            size_hex = match1.group(2)
            file_path = match1.group(3).strip()
            self._add_file_size(file_path, size_hex, segment_name)
            return True
            
        # 匹配分行格式的第二行（地址、大小、文件路径）
        pattern2 = r'^\s+0x[0-9a-fA-F]+\s+0x([1-9a-fA-F][0-9a-fA-F]*)\s+(.*)$'
        match2 = re.match(pattern2, line)
        if match2:
            size_hex = match2.group(1)
            file_path = match2.group(2).strip()
            self._add_file_size(file_path, size_hex, segment_name)
            return True
            
        return False
    
    def _add_file_size(self, file_path, size_hex, segment_name):
        """添加文件大小统计"""
        try:
            size = int(size_hex, 16)
        except ValueError:
            return
        
        if size == 0:
            return
        
        # 提取文件名
        if '.a(' in file_path:
            # 静态库格式: /path/lib.a(file.o)
            filename = file_path.split('/')[-1]  # 获取lib.a(file.o)部分
        else:
            # 普通路径
            filename = Path(file_path).name
        
        # 提取完整的原始目录路径
        directory_paths = self._extract_all_directory_levels(file_path)
        
        # 更新文件统计
        self.segments[segment_name]['files'][filename] += size
        
        # 记录文件到目录的映射关系
        if filename not in self.file_to_directories[segment_name]:
            self.file_to_directories[segment_name][filename] = directory_paths.copy()
        
        # 更新目录统计（所有层级）
        for directory_path in directory_paths:
            self.segments[segment_name]['directories'][directory_path]['size'] += size
            
            # 对于文件计数，只有当这是该文件在该段中的第一次出现时才计数
            segment_file_key = f"{segment_name}::{directory_path}::{filename}"
            if not hasattr(self, '_segment_file_counts'):
                self._segment_file_counts = set()
            
            if segment_file_key not in self._segment_file_counts:
                self.segments[segment_name]['directories'][directory_path]['file_count'] += 1
                self._segment_file_counts.add(segment_file_key)
    
    def _extract_all_directory_levels(self, file_path):
        """提取文件路径的所有层级目录"""
        # 提取完整的原始目录路径
        full_original_path = self._extract_full_original_path(file_path)
        
        if not full_original_path:
            return ['standalone']
        
        # 将完整路径按/分割
        path_parts = full_original_path.split('/')
        
        # 生成所有层级的路径
        directory_paths = []
        for i in range(1, min(len(path_parts) + 1, self.max_dir_levels + 1)):
            level_path = '/'.join(path_parts[:i])
            directory_paths.append(level_path)
        
        return directory_paths if directory_paths else ['standalone']
    
    def _extract_full_original_path(self, file_path):
        """提取.o文件的完整原始目录路径"""
        # 处理静态库格式: /path/to/lib.a(AwtkApplication/src/dreame/cardPage/home/dreHome.c.data...o)
        if '.a(' in file_path:
            # 提取括号内的.o文件路径
            o_file_part = file_path.split('.a(')[1].rstrip(')')
            
            # 从.o文件路径中提取原始目录结构
            if '/' in o_file_part:
                # 分割路径并去掉文件名
                parts = o_file_part.split('/')
                # 取目录部分，去掉最后的文件名
                if len(parts) > 1:
                    # 返回完整的目录路径
                    return '/'.join(parts[:-1])
            else:
                # 如果没有目录结构，使用文件名作为目录
                file_name = o_file_part.split('.')[0] if '.' in o_file_part else o_file_part
                return file_name
        
        # 处理完整路径格式（非静态库）
        elif 'WB100-SDK/' in file_path:
            # 提取WB100-SDK后的路径
            sdk_part = file_path.split('WB100-SDK/')[-1]
            parts = sdk_part.split('/')
            
            # 去掉文件名，只保留目录部分
            if len(parts) > 1:
                return '/'.join(parts[:-1])  # 去掉文件名
        
        # 处理其他路径
        elif '/' in file_path:
            parts = file_path.split('/')
            # 找到有意义的目录层级
            meaningful_parts = []
            for part in parts[:-1]:  # 去掉文件名
                if part and not part.startswith('data') and not part.startswith('tmp'):
                    meaningful_parts.append(part)
            if meaningful_parts:
                return '/'.join(meaningful_parts)
        
        # 如果没有提取到任何目录，返回空
        return ''
    
    def format_size(self, size_bytes):
        """格式化大小显示"""
        if size_bytes >= 1024 * 1024:
            return f"{size_bytes / (1024 * 1024):.2f} MB (0x{size_bytes:x} bytes)"
        elif size_bytes >= 1024:
            return f"{size_bytes / 1024:.2f} KB (0x{size_bytes:x} bytes)"
        else:
            return f"{size_bytes} bytes (0x{size_bytes:x})"
    
    def _build_directory_tree(self, directories, segment_files, segment_name):
        """构建完整的目录层级树结构，包含文件信息"""
        tree = {}
        
        # 构建树结构
        for dir_path, dir_info in directories.items():
            parts = dir_path.split('/')
            current = tree
            
            for i, part in enumerate(parts):
                if part not in current:
                    current[part] = {
                        '_info': {'size': 0, 'file_count': 0, 'path': '/'.join(parts[:i+1])},
                        '_children': {},
                        '_files': []  # 添加文件列表
                    }
                current = current[part]['_children']
            
            # 在叶子节点设置实际数据
            leaf_node = tree
            for part in parts[:-1]:
                leaf_node = leaf_node[part]['_children']
            if parts[-1] in leaf_node:
                leaf_node[parts[-1]]['_info'] = {
                    'size': dir_info['size'],
                    'file_count': dir_info['file_count'],
                    'path': dir_path
                }
        
        # 为每个目录节点收集文件信息  
        self._collect_files_for_directories(tree, segment_files, directories, segment_name)
        
        # 从叶子节点向上汇总数据
        self._aggregate_tree_data(tree)
        
        return tree
    
    def _collect_files_for_directories(self, tree, segment_files, directories, segment_name):
        """为每个目录节点收集对应的文件信息"""
        # 为每个目录收集属于该目录的文件
        for dir_path in directories:
            dir_parts = dir_path.split('/')
            
            # 找到对应的树节点
            current = tree
            for part in dir_parts[:-1]:
                if part in current:
                    current = current[part]['_children']
                else:
                    break
            
            # 如果找到了对应的目录节点
            if dir_parts[-1] in current:
                dir_node = current[dir_parts[-1]]
                
                # 收集属于这个目录的文件
                for filename, size in segment_files.items():
                    # 检查文件是否属于这个目录
                    if self._file_belongs_to_directory(filename, dir_path, segment_name):
                        dir_node['_files'].append({
                            'name': filename,
                            'size': size,
                            'size_formatted': self.format_size(size)
                        })
                
                # 按大小排序文件
                dir_node['_files'].sort(key=lambda x: x['size'], reverse=True)
    
    def _file_belongs_to_directory(self, filename, dir_path, segment_name):
        """判断文件是否属于指定目录（只属于最深层目录）"""
        if segment_name in self.file_to_directories and filename in self.file_to_directories[segment_name]:
            # 文件只属于最深层目录，即目录路径列表中的最后一个（最长的路径）
            file_directories = self.file_to_directories[segment_name][filename]
            if file_directories:
                # 找到最深层目录（路径最长的）
                deepest_directory = max(file_directories, key=len)
                return dir_path == deepest_directory
        return False
    
    def _aggregate_tree_data(self, tree):
        """从底向上汇总目录统计信息"""
        for node_name, node_data in tree.items():
            if node_data['_children']:
                # 先递归处理子节点
                self._aggregate_tree_data(node_data['_children'])
                
                # 汇总子节点数据到当前节点
                total_size = 0
                total_files = 0
                
                for child_name, child_data in node_data['_children'].items():
                    total_size += child_data['_info']['size']
                    total_files += child_data['_info']['file_count']
                
                # 如果当前节点没有直接的数据，使用汇总数据
                if node_data['_info']['size'] == 0:
                    node_data['_info']['size'] = total_size
                    node_data['_info']['file_count'] = total_files
    
    def generate_html_report(self, output_path, map_file_path):
        """生成HTML报告"""
        html_content = self._create_html_template()
        
        # 生成段总览数据
        segments_data = self._prepare_segments_data()
        
        # 生成目录树数据
        directory_trees = self._prepare_directory_trees()
        
        # 替换模板中的数据
        html_content = html_content.replace('{{SEGMENTS_DATA}}', json.dumps(segments_data, ensure_ascii=False))
        html_content = html_content.replace('{{DIRECTORY_TREES}}', json.dumps(directory_trees, ensure_ascii=False))
        html_content = html_content.replace('{{MAP_FILE_NAME}}', Path(map_file_path).name)
        html_content = html_content.replace('{{GENERATION_TIME}}', datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
        
        # 写入HTML文件
        try:
            with open(output_path, 'w', encoding='utf-8') as f:
                f.write(html_content)
            print(f"HTML报告已生成: {output_path}")
            return True
        except Exception as e:
            print(f"生成HTML报告失败: {e}")
            return False
    
    def _prepare_segments_data(self):
        """准备段总览数据"""
        segments_list = []
        total_size = 0
        
        # 按大小排序段
        sorted_segments = sorted(self.segments.items(), key=lambda x: x[1]['size'], reverse=True)
        
        for segment_name, segment_info in sorted_segments:
            size = segment_info['size']
            total_size += size
            
            segments_list.append({
                'name': segment_name,
                'start_addr': f"0x{segment_info['start_addr']:x}",
                'size': size,
                'size_formatted': self.format_size(size),
                'file_count': len(segment_info['files'])
            })
        
        # 计算占比
        for segment in segments_list:
            segment['percentage'] = (segment['size'] / total_size * 100) if total_size > 0 else 0
        
        return {
            'segments': segments_list,
            'total_size': total_size,
            'total_size_formatted': self.format_size(total_size)
        }
    
    def _prepare_directory_trees(self):
        """准备目录树数据"""
        directory_trees = {}
        
        for segment_name, segment_info in self.segments.items():
            if segment_info['directories']:
                tree = self._build_directory_tree(segment_info['directories'], 
                                                segment_info['files'], 
                                                segment_name)
                directory_trees[segment_name] = {
                    'tree': tree,
                    'total_size': segment_info['size'],
                    'total_size_formatted': self.format_size(segment_info['size'])
                }
        return directory_trees
    
    def _create_html_template(self):
        """创建HTML模板"""
        return """<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Map文件分析报告 - {{MAP_FILE_NAME}}</title>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        
        body {
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', 'Roboto', sans-serif;
            line-height: 1.6;
            color: #333;
            background-color: #f5f5f5;
        }
        
        .container {
            max-width: 1200px;
            margin: 0 auto;
            padding: 20px;
        }
        
        .header {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: 30px;
            border-radius: 10px;
            margin-bottom: 30px;
            text-align: center;
        }
        
        .header h1 { font-size: 2.5em; margin-bottom: 10px; }
        .header p { font-size: 1.1em; opacity: 0.9; }
        
        .section {
            background: white;
            border-radius: 10px;
            padding: 25px;
            margin-bottom: 30px;
            box-shadow: 0 2px 10px rgba(0,0,0,0.1);
        }
        
        .section h2 {
            color: #444;
            margin-bottom: 20px;
            padding-bottom: 10px;
            border-bottom: 3px solid #667eea;
            font-size: 1.8em;
        }
        
        .segments-table {
            width: 100%;
            border-collapse: collapse;
            margin-top: 15px;
        }
        
        .segments-table th,
        .segments-table td {
            padding: 12px;
            text-align: left;
            border-bottom: 1px solid #ddd;
        }
        
        .segments-table th {
            background: linear-gradient(135deg, #f8f9ff 0%, #e8f0ff 100%);
            font-weight: 600;
            color: #555;
        }
        
        .segments-table tr:hover {
            background-color: #f8f9ff;
        }
        
        .percentage-bar {
            width: 100px;
            height: 20px;
            background: #f0f0f0;
            border-radius: 10px;
            overflow: hidden;
            position: relative;
        }
        
        .percentage-fill {
            height: 100%;
            background: linear-gradient(90deg, #667eea, #764ba2);
            border-radius: 10px;
            transition: width 0.3s ease;
        }
        
        .tree-container {
            margin-bottom: 30px;
        }
        
        .tree-header {
            background: linear-gradient(135deg, #f8f9ff 0%, #e8f0ff 100%);
            padding: 15px;
            border-radius: 8px;
            margin-bottom: 15px;
            font-weight: 600;
            color: #555;
        }
        
        .tree {
            font-family: 'Monaco', 'Menlo', 'Ubuntu Mono', monospace;
            font-size: 14px;
            background: #fafafa;
            border-radius: 8px;
            padding: 20px;
            overflow-x: auto;
        }
        
        .tree-node {
            margin: 2px 0;
            cursor: pointer;
            padding: 2px 5px;
            border-radius: 3px;
            transition: background-color 0.2s;
        }
        
        .tree-node:hover {
            background-color: #e8f0ff;
        }
        
        .tree-node.expanded > .tree-children {
            display: block !important;
        }
        
        .tree-children {
            display: none;
            margin-left: 20px;
        }
        
        .tree-toggle {
            display: inline-block;
            width: 16px;
            text-align: center;
            color: #666;
            user-select: none;
        }
        
        .tree-content {
            display: inline-block;
        }
        
        .tree-name {
            color: #2563eb;
            font-weight: 500;
        }
        
        .tree-size {
            color: #059669;
            font-weight: 600;
        }
        
        .tree-count {
            color: #7c3aed;
        }
        
        .tree-percentage {
            color: #dc2626;
        }
        
        .tree-file {
            margin: 1px 0;
            padding: 2px 5px;
            border-radius: 3px;
            font-size: 13px;
            color: #555;
        }
        
        .tree-file:hover {
            background-color: #f0f8ff;
        }
        
        .tab-container {
            margin-bottom: 20px;
        }
        
        .tabs {
            display: flex;
            border-bottom: 2px solid #e5e7eb;
            margin-bottom: 20px;
        }
        
        .tab {
            padding: 12px 24px;
            cursor: pointer;
            border: none;
            background: none;
            font-size: 16px;
            color: #6b7280;
            border-bottom: 3px solid transparent;
            transition: all 0.2s;
        }
        
        .tab.active {
            color: #667eea;
            border-bottom-color: #667eea;
            font-weight: 600;
        }
        
        .tab:hover {
            color: #667eea;
            background: #f8f9ff;
        }
        
        .tab-content {
            display: none;
        }
        
        .tab-content.active {
            display: block;
        }
        
        .summary-stats {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
            gap: 20px;
            margin-bottom: 20px;
        }
        
        .stat-card {
            background: linear-gradient(135deg, #f8f9ff 0%, #e8f0ff 100%);
            padding: 20px;
            border-radius: 10px;
            text-align: center;
        }
        
        .stat-value {
            font-size: 2em;
            font-weight: bold;
            color: #667eea;
            margin-bottom: 5px;
        }
        
        .stat-label {
            color: #6b7280;
            font-size: 0.9em;
        }
        
        @media (max-width: 768px) {
            .container { padding: 10px; }
            .header { padding: 20px; }
            .header h1 { font-size: 2em; }
            .section { padding: 15px; }
            .segments-table { font-size: 14px; }
            .tree { padding: 15px; font-size: 12px; }
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>Map文件分析报告</h1>
            <p>文件: {{MAP_FILE_NAME}} | 生成时间: {{GENERATION_TIME}}</p>
        </div>
        
        <div class="section">
            <h2>📊 段总览</h2>
            <div class="summary-stats">
                <div class="stat-card">
                    <div class="stat-value" id="total-segments">-</div>
                    <div class="stat-label">总段数</div>
                </div>
                <div class="stat-card">
                    <div class="stat-value" id="total-size">-</div>
                    <div class="stat-label">总大小</div>
                </div>
                <div class="stat-card">
                    <div class="stat-value" id="largest-segment">-</div>
                    <div class="stat-label">最大段</div>
                </div>
            </div>
            
            <table class="segments-table">
                <thead>
                    <tr>
                        <th>段名称</th>
                        <th>起始地址</th>
                        <th>大小</th>
                        <th>文件数</th>
                        <th>占比</th>
                        <th>占比图</th>
                    </tr>
                </thead>
                <tbody id="segments-tbody">
                </tbody>
            </table>
        </div>
        
        <div class="section">
            <h2>🌳 目录树状结构</h2>
            <div class="tab-container">
                <div class="tabs" id="segment-tabs">
                </div>
                <div id="tree-content">
                </div>
            </div>
        </div>
    </div>

    <script>
        // 数据
        const segmentsData = {{SEGMENTS_DATA}};
        const directoryTrees = {{DIRECTORY_TREES}};
        
        // 初始化页面
        document.addEventListener('DOMContentLoaded', function() {
            initializeSegmentsTable();
            initializeDirectoryTrees();
        });
        
        function initializeSegmentsTable() {
            // 更新统计信息
            document.getElementById('total-segments').textContent = segmentsData.segments.length;
            document.getElementById('total-size').textContent = segmentsData.total_size_formatted;
            document.getElementById('largest-segment').textContent = segmentsData.segments[0]?.name || '-';
            
            // 填充表格
            const tbody = document.getElementById('segments-tbody');
            tbody.innerHTML = '';
            
            segmentsData.segments.forEach(segment => {
                const row = document.createElement('tr');
                row.innerHTML = `
                    <td><strong>${segment.name}</strong></td>
                    <td><code>${segment.start_addr}</code></td>
                    <td>${segment.size_formatted}</td>
                    <td>${segment.file_count.toLocaleString()}</td>
                    <td>${segment.percentage.toFixed(1)}%</td>
                    <td>
                        <div class="percentage-bar">
                            <div class="percentage-fill" style="width: ${Math.min(segment.percentage, 100)}%"></div>
                        </div>
                    </td>
                `;
                tbody.appendChild(row);
            });
        }
        
        function initializeDirectoryTrees() {
            const tabs = document.getElementById('segment-tabs');
            const content = document.getElementById('tree-content');
            
            tabs.innerHTML = '';
            content.innerHTML = '';
            
            const segmentNames = Object.keys(directoryTrees);
            
            segmentNames.forEach((segmentName, index) => {
                // 创建标签页
                const tab = document.createElement('button');
                tab.className = 'tab' + (index === 0 ? ' active' : '');
                tab.textContent = segmentName;
                tab.onclick = () => switchTab(segmentName);
                tabs.appendChild(tab);
                
                // 创建内容
                const tabContent = document.createElement('div');
                tabContent.className = 'tab-content' + (index === 0 ? ' active' : '');
                tabContent.id = `tab-${segmentName}`;
                
                const treeData = directoryTrees[segmentName];
                tabContent.innerHTML = `
                    <div class="tree-header">
                        ${segmentName} - 总大小: ${treeData.total_size_formatted}
                    </div>
                    <div class="tree" id="tree-${segmentName}">
                        ${generateTreeHtml(treeData.tree, treeData.total_size)}
                    </div>
                `;
                
                content.appendChild(tabContent);
            });
            
            // 添加树节点点击事件
            setTimeout(() => {
                addTreeEventListeners();
            }, 100);
        }
        
        function switchTab(segmentName) {
            // 更新标签页状态
            document.querySelectorAll('.tab').forEach(tab => {
                tab.classList.remove('active');
            });
            event.target.classList.add('active');
            
            // 更新内容显示
            document.querySelectorAll('.tab-content').forEach(content => {
                content.classList.remove('active');
            });
            document.getElementById(`tab-${segmentName}`).classList.add('active');
        }
        
        function generateTreeHtml(tree, totalSize, level = 0) {
            let html = '';
            
            // 按大小排序
            const sortedEntries = Object.entries(tree).sort((a, b) => {
                return b[1]._info.size - a[1]._info.size;
            });
            
            sortedEntries.forEach(([name, data]) => {
                const hasChildren = Object.keys(data._children).length > 0;
                const hasFiles = data._files && data._files.length > 0;
                const percentage = totalSize > 0 ? (data._info.size / totalSize * 100) : 0;
                
                // 显示目录节点
                html += `
                    <div class="tree-node" data-level="${level}">
                        <span class="tree-toggle">${(hasChildren || hasFiles) ? '▶' : '  '}</span>
                        <span class="tree-content">
                            <span class="tree-name">📁 ${name}</span>
                            <span class="tree-size">${formatSize(data._info.size)}</span>
                            <span class="tree-count">(${data._info.file_count} files)</span>
                            <span class="tree-percentage">${percentage.toFixed(1)}%</span>
                        </span>
                        <div class="tree-children">
                            ${hasFiles ? generateFilesHtml(data._files, totalSize) : ''}
                            ${hasChildren ? generateTreeHtml(data._children, totalSize, level + 1) : ''}
                        </div>
                    </div>
                `;
            });
            
            return html;
        }
        
        function generateFilesHtml(files, totalSize) {
            let html = '';
            
            // 显示前10个最大的文件
            const topFiles = files.slice(0, 10);
            
            topFiles.forEach(file => {
                const percentage = totalSize > 0 ? (file.size / totalSize * 100) : 0;
                html += `
                    <div class="tree-file" style="margin-left: 40px;">
                        <span class="tree-content">
                            <span class="tree-name">📄 ${file.name}</span>
                            <span class="tree-size">${file.size_formatted}</span>
                            <span class="tree-percentage">${percentage.toFixed(2)}%</span>
                        </span>
                    </div>
                `;
            });
            
            // 如果有更多文件，显示提示
            if (files.length > 10) {
                html += `
                    <div class="tree-file" style="margin-left: 40px; color: #888; font-style: italic;">
                        ... 和 ${files.length - 10} 个其他文件
                    </div>
                `;
            }
            
            return html;
        }
        
        function addTreeEventListeners() {
            document.querySelectorAll('.tree-node').forEach(node => {
                const toggle = node.querySelector('.tree-toggle');
                if (toggle && toggle.textContent.trim() === '▶') {
                    node.style.cursor = 'pointer';
                    node.addEventListener('click', function(e) {
                        e.stopPropagation();
                        toggleTreeNode(this);
                    });
                }
            });
        }
        
        function toggleTreeNode(node) {
            const toggle = node.querySelector('.tree-toggle');
            const children = node.querySelector('.tree-children');
            
            if (children) {
                if (node.classList.contains('expanded')) {
                    node.classList.remove('expanded');
                    toggle.textContent = '▶';
                    children.style.display = 'none';
                } else {
                    node.classList.add('expanded');
                    toggle.textContent = '▼';
                    children.style.display = 'block';
                }
            }
        }
        
        function formatSize(bytes) {
            if (bytes >= 1024 * 1024) {
                return `${(bytes / (1024 * 1024)).toFixed(2)} MB`;
            } else if (bytes >= 1024) {
                return `${(bytes / 1024).toFixed(2)} KB`;
            } else {
                return `${bytes} bytes`;
            }
        }
    </script>
</body>
</html>"""


def main():
    parser = argparse.ArgumentParser(
        description='Map文件HTML分析器 - 生成HTML格式的分析报告',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
示例:
  python map_html_analyzer.py nuttx_a7.map                           # 生成HTML报告
  python map_html_analyzer.py nuttx_a7.map -o report.html           # 指定输出文件名
  python map_html_analyzer.py --include-debug nuttx_a7.map          # 包含debug段
  python map_html_analyzer.py -d -l 5 nuttx_a7.map                  # 包含debug段，最大5层目录
        """
    )
    
    parser.add_argument('map_file', help='Map文件路径')
    parser.add_argument('-o', '--output', default='map_report.html', help='输出HTML文件名 (默认: map_report.html)')
    parser.add_argument('--include-debug', '-d', action='store_true', 
                       help='包含debug相关段的输出 (默认隐藏debug段)')
    parser.add_argument('--max-dir-levels', '-l', type=int, default=10, metavar='N',
                       help='最大目录层级数量 (默认10层)')
    
    args = parser.parse_args()
    
    if not Path(args.map_file).exists():
        print(f"错误: 文件 {args.map_file} 不存在")
        sys.exit(1)
    
    analyzer = MapHtmlAnalyzer(include_debug=args.include_debug, 
                              max_dir_levels=args.max_dir_levels)
    
    print(f"正在解析map文件: {args.map_file}")
    if analyzer.parse_map_file(args.map_file):
        print("解析完成，正在生成HTML报告...")
        if analyzer.generate_html_report(args.output, args.map_file):
            print(f"✅ HTML报告生成成功: {args.output}")
        else:
            print("❌ HTML报告生成失败")
            sys.exit(1)
    else:
        print("❌ map文件解析失败")
        sys.exit(1)


if __name__ == "__main__":
    main()