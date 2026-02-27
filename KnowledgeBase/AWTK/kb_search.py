#!/usr/bin/env python3
import json
import re
import os
import argparse
from typing import List, Dict, Optional

class AWTKKnowledgeBase:
    def __init__(self, kb_dir: str):
        self.kb_dir = kb_dir
        self.search_index = None
        self.api_index = None
        self._load_index()
    
    def _load_index(self):
        """加载索引文件"""
        search_path = os.path.join(self.kb_dir, 'search_index.json')
        api_path = os.path.join(self.kb_dir, 'api_index.json')
        
        if os.path.exists(search_path):
            with open(search_path, 'r', encoding='utf-8') as f:
                self.search_index = json.load(f)
        else:
            print(f"警告: 搜索索引文件不存在: {search_path}")
        
        if os.path.exists(api_path):
            with open(api_path, 'r', encoding='utf-8') as f:
                self.api_index = json.load(f)
        else:
            print(f"警告: API 索引文件不存在: {api_path}")
    
    def _split_keywords(self, text: str) -> List[str]:
        if not text:
            return []
        tokens = re.split(r'[\s,;，。！？、()\[\]{}<>：:]+', text.lower())
        return [t for t in tokens if t]
    
    def search_by_keyword(self, keyword: str, max_results: int = 20) -> List[Dict]:
        """按关键词搜索"""
        if not self.search_index:
            return []
        
        results = []
        keyword_lower = keyword.lower()
        tokens = self._split_keywords(keyword)
        
        for item in self.search_index:
            title = item.get('title', '') or ''
            description = item.get('description', '') or ''
            functions = item.get('functions', []) or []
            types = item.get('types', []) or []
            title_lower = title.lower()
            description_lower = description.lower()
            score = 0
            if keyword_lower and (keyword_lower in title_lower or keyword_lower in description_lower):
                score += 5
            for token in tokens:
                if token in title_lower:
                    score += 5
                if token in description_lower:
                    score += 3
                for func in functions:
                    func_lower = func.lower()
                    if token in func_lower:
                        score += 8
                for t in types:
                    type_lower = t.lower()
                    if token in type_lower:
                        score += 6
            if score > 0:
                item_with_score = dict(item)
                item_with_score['_score'] = score
                results.append(item_with_score)
        
        results.sort(key=lambda x: x.get('_score', 0), reverse=True)
        return results[:max_results]
    
    def search_by_function(self, function_name: str) -> List[Dict]:
        """按函数名搜索"""
        if not self.search_index:
            return []
        
        results = []
        target = function_name.lower()
        
        for item in self.search_index:
            functions = item.get('functions', []) or []
            for func in functions:
                func_lower = func.lower()
                if func_lower == target or target in func_lower:
                    results.append(item)
                    break
        
        return results
    
    def search_by_type(self, type_name: str) -> List[Dict]:
        """按类型名搜索"""
        if not self.search_index:
            return []
        
        results = []
        target = type_name.lower()
        
        for item in self.search_index:
            types = item.get('types', []) or []
            for t in types:
                type_lower = t.lower()
                if type_lower == target or target in type_lower:
                    results.append(item)
                    break
        
        return results
    
    def search_auto(self, question: str, max_results: int = 20) -> List[Dict]:
        if not self.search_index:
            return []
        results = []
        seen_files = set()
        pattern = r'\b[a-zA-Z_][a-zA-Z0-9_]*\b'
        candidates = set(re.findall(pattern, question))
        for name in candidates:
            func_matches = self.search_by_function(name)
            for item in func_matches:
                file_id = item.get('file')
                if file_id not in seen_files:
                    results.append(item)
                    seen_files.add(file_id)
            type_matches = self.search_by_type(name)
            for item in type_matches:
                file_id = item.get('file')
                if file_id not in seen_files:
                    results.append(item)
                    seen_files.add(file_id)
            if len(results) >= max_results:
                return results[:max_results]
        keyword_matches = self.search_by_keyword(question, max_results=max_results)
        for item in keyword_matches:
            file_id = item.get('file')
            if file_id not in seen_files:
                results.append(item)
                seen_files.add(file_id)
            if len(results) >= max_results:
                break
        return results[:max_results]
    
    def get_document(self, filename: str) -> Optional[str]:
        """获取文档内容"""
        md_path = os.path.join(self.kb_dir, filename)
        
        if os.path.exists(md_path):
            with open(md_path, 'r', encoding='utf-8', errors='ignore') as f:
                return f.read()
        
        return None
    
    def get_api_details(self, filename: str) -> Optional[Dict]:
        """获取 API 详细信息"""
        if not self.api_index:
            return None
        
        for api in self.api_index.get('api_index', []):
            if api['filename'] == filename:
                return api
        return None
    
    def get_all_categories(self) -> List[str]:
        """获取所有分类"""
        if not self.api_index:
            return []
        return list(self.api_index.get('categories', {}).keys())
    
    def get_category_files(self, category: str) -> List[str]:
        """获取分类下的文件"""
        if not self.api_index:
            return []
        return self.api_index.get('categories', {}).get(category, [])

def detect_awtk_keywords(text: str) -> List[str]:
    keywords = []
    patterns = [
        r'awtk',
        r'widget',
        r'\btk_\w+\b',
        r'\b[a-zA-Z_]\w*_widget\w*\b',
    ]
    for pattern in patterns:
        matches = re.findall(pattern, text, re.IGNORECASE)
        keywords.extend(matches)
    return list(set(keywords))

def should_use_knowledgebase(text: str) -> bool:
    return len(detect_awtk_keywords(text)) > 0

def main():
    kb_dir = "/home/xl/dreame/AIcode/KnowledgeBase/AWTK"
    kb = AWTKKnowledgeBase(kb_dir)

    parser = argparse.ArgumentParser(description="AWTK API 知识库搜索工具")
    parser.add_argument("keyword", nargs="?", help="要搜索的关键词或问题")
    parser.add_argument("--keyword", dest="keyword_opt", help="要搜索的关键词或问题")
    parser.add_argument("--max-results", type=int, default=20, help="返回的最大结果数")
    args = parser.parse_args()

    keyword = args.keyword_opt or args.keyword

    if keyword:
        print("=" * 60)
        print("AWTK API 知识库搜索工具")
        print("=" * 60)
        print(f"\n查询: {keyword}")
        results = kb.search_auto(keyword, max_results=args.max_results)
        print(f"\n找到 {len(results)} 个结果:")
        for i, item in enumerate(results[: args.max_results], 1):
            title = item.get("title", "")
            file_name = item.get("file")
            functions = item.get("functions") or []
            description = item.get("description") or ""
            print(f"{i}. {title}")
            if file_name:
                print(f"   文件: {file_name}")
            if functions:
                print(f"   函数: {', '.join(functions[:3])}")
            if description:
                snippet = description
                if len(snippet) > 100:
                    snippet = snippet[:100] + "..."
                print(f"   描述: {snippet}")
        return

    print("=" * 60)
    print("AWTK API 知识库搜索工具")
    print("=" * 60)

    while True:
        print("\n请选择搜索方式:")
        print("1. 按关键词搜索")
        print("2. 按函数名搜索")
        print("3. 按类型名搜索")
        print("4. 查看分类")
        print("0. 退出")

        choice = input("\n请输入选择: ").strip()

        if choice == "0":
            break
        elif choice == "1":
            keyword = input("请输入关键词: ").strip()
            results = kb.search_by_keyword(keyword)
            print(f"\n找到 {len(results)} 个结果:")
            for i, item in enumerate(results[:10], 1):
                print(f"{i}. {item['title']}")
                print(f"   文件: {item['file']}")
                if item['functions']:
                    print(f"   函数: {', '.join(item['functions'][:3])}")
                if item['description']:
                    print(f"   描述: {item['description'][:100]}...")
        elif choice == "2":
            func_name = input("请输入函数名: ").strip()
            results = kb.search_by_function(func_name)
            print(f"\n找到 {len(results)} 个结果:")
            for i, item in enumerate(results[:10], 1):
                print(f"{i}. {item['title']}")
                print(f"   文件: {item['file']}")
        elif choice == "3":
            type_name = input("请输入类型名: ").strip()
            results = kb.search_by_type(type_name)
            print(f"\n找到 {len(results)} 个结果:")
            for i, item in enumerate(results[:10], 1):
                print(f"{i}. {item['title']}")
                print(f"   文件: {item['file']}")
        elif choice == "4":
            categories = kb.get_all_categories()
            print(f"\n分类列表:")
            for cat in categories:
                files = kb.get_category_files(cat)
                print(f"  - {cat}: {len(files)} 个文件")

if __name__ == "__main__":
    main()
