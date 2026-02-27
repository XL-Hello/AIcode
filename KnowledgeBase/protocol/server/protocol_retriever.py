#!/usr/bin/env python3
"""
本地知识库检索工具 - 协议检索
用于检索 /home/xl/dreame/AIcode/KnowledgeBase/protocol/server 下的协议文档
"""

import os
import re
import json
import argparse
from collections import defaultdict

class ProtocolRetriever:
    def __init__(self, base_path):
        self.base_path = base_path
        self.index = {}
        self.build_index()

    def build_index(self):
        """构建文档索引"""
        docs_path = os.path.join(self.base_path, 'docs')
        for root, dirs, files in os.walk(docs_path):
            for file in files:
                if file.endswith('.md'):
                    file_path = os.path.join(root, file)
                    rel_path = os.path.relpath(file_path, self.base_path)
                    with open(file_path, 'r', encoding='utf-8') as f:
                        content = f.read()
                        self.index[rel_path] = {
                            'content': content,
                            'lines': content.split('\n'),
                            'keywords': self.extract_keywords(content)
                        }

    def extract_keywords(self, content):
        """提取关键词"""
        # 简单提取：intent, 协议, 设备等
        keywords = set()
        patterns = [
            r'intent\s*=\s*["\'](\w+)["\']',
            r'设备',
            r'控制',
            r'报告',
            r'绑定',
            r'Token',
            r'MQTT',
            r'HTTPS'
        ]
        for pattern in patterns:
            matches = re.findall(pattern, content, re.IGNORECASE)
            keywords.update(matches)
        return list(keywords)

    def search(self, query, top_n=3):
        """搜索相关文档"""
        results = []
        query_lower = query.lower()

        for file_path, data in self.index.items():
            score = 0
            matches = []

            # 文件名匹配
            if query_lower in file_path.lower():
                score += 10

            # 关键词匹配
            for kw in data['keywords']:
                if kw.lower() in query_lower or query_lower in kw.lower():
                    score += 5

            # 内容匹配
            for i, line in enumerate(data['lines']):
                if query_lower in line.lower():
                    score += 1
                    matches.append(f"行{i+1}: {line.strip()}")

            if score > 0:
                results.append({
                    'file': file_path,
                    'score': score,
                    'matches': matches[:3]  # 最多3个匹配片段
                })

        # 按分数排序
        results.sort(key=lambda x: x['score'], reverse=True)
        return results[:top_n]

    def get_document_content(self, file_path):
        """获取文档内容"""
        if file_path in self.index:
            return self.index[file_path]['content']
        return None

# 使用示例
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='本地知识库协议检索工具')
    parser.add_argument('query', help='检索关键词')
    parser.add_argument('--top_n', type=int, default=3, help='返回结果数量 (默认3)')

    args = parser.parse_args()

    retriever = ProtocolRetriever('/home/xl/dreame/AIcode/KnowledgeBase/protocol/server')
    results = retriever.search(args.query, args.top_n)

    print(f"检索关键词: {args.query}")
    print(f"检索结果 ({len(results)} 个):")
    for i, result in enumerate(results, 1):
        print(f"{i}. {result['file']} (相关度: {result['score']})")
        for match in result['matches']:
            print(f"   {match}")
        print()