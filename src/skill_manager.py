#!/usr/bin/env python3
"""
AIcode Skills Manager
管理和使用开发技能的核心模块
"""

import json
import os
from pathlib import Path
from typing import Dict, List, Optional, Any


class Skill:
    """表示单个技能的类"""
    
    def __init__(self, name: str, description: str, category: str, 
                 implementation: str, examples: Optional[List[str]] = None,
                 metadata: Optional[Dict[str, Any]] = None):
        self.name = name
        self.description = description
        self.category = category
        self.implementation = implementation
        self.examples = examples or []
        self.metadata = metadata or {}
    
    def to_dict(self) -> Dict[str, Any]:
        """将技能转换为字典格式"""
        return {
            'name': self.name,
            'description': self.description,
            'category': self.category,
            'implementation': self.implementation,
            'examples': self.examples,
            'metadata': self.metadata
        }
    
    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'Skill':
        """从字典创建技能对象"""
        return cls(
            name=data['name'],
            description=data['description'],
            category=data['category'],
            implementation=data['implementation'],
            examples=data.get('examples', []),
            metadata=data.get('metadata', {})
        )


class SkillManager:
    """技能管理器，负责加载、存储和管理技能"""
    
    def __init__(self, skills_dir: Optional[str] = None):
        if skills_dir is None:
            # 默认使用相对于此文件的skills目录
            base_dir = Path(__file__).parent.parent
            self.skills_dir = base_dir / 'skills'
        else:
            self.skills_dir = Path(skills_dir)
        
        self.skills: Dict[str, Skill] = {}
        self.categories: Dict[str, List[str]] = {}
    
    def load_skill_from_file(self, filepath: Path) -> Optional[Skill]:
        """从文件加载单个技能"""
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                data = json.load(f)
                skill = Skill.from_dict(data)
                return skill
        except Exception as e:
            print(f"Error loading skill from {filepath}: {e}")
            return None
    
    def load_all_skills(self) -> int:
        """加载所有技能文件"""
        if not self.skills_dir.exists():
            print(f"Skills directory not found: {self.skills_dir}")
            return 0
        
        loaded_count = 0
        for filepath in self.skills_dir.rglob('*.json'):
            skill = self.load_skill_from_file(filepath)
            if skill:
                self.add_skill(skill)
                loaded_count += 1
        
        return loaded_count
    
    def add_skill(self, skill: Skill):
        """添加技能到管理器"""
        self.skills[skill.name] = skill
        
        # 更新分类索引
        if skill.category not in self.categories:
            self.categories[skill.category] = []
        if skill.name not in self.categories[skill.category]:
            self.categories[skill.category].append(skill.name)
    
    def get_skill(self, name: str) -> Optional[Skill]:
        """根据名称获取技能"""
        return self.skills.get(name)
    
    def get_skills_by_category(self, category: str) -> List[Skill]:
        """获取特定分类的所有技能"""
        skill_names = self.categories.get(category, [])
        return [self.skills[name] for name in skill_names if name in self.skills]
    
    def list_all_skills(self) -> List[Skill]:
        """列出所有技能"""
        return list(self.skills.values())
    
    def list_categories(self) -> List[str]:
        """列出所有分类"""
        return list(self.categories.keys())
    
    def search_skills(self, keyword: str) -> List[Skill]:
        """搜索技能（按名称或描述）"""
        keyword = keyword.lower()
        results = []
        for skill in self.skills.values():
            if (keyword in skill.name.lower() or 
                keyword in skill.description.lower()):
                results.append(skill)
        return results
    
    def save_skill(self, skill: Skill, filepath: Optional[Path] = None):
        """保存技能到文件"""
        if filepath is None:
            self.skills_dir.mkdir(parents=True, exist_ok=True)
            filepath = self.skills_dir / f"{skill.name}.json"
        
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(skill.to_dict(), f, indent=2, ensure_ascii=False)
    
    def print_skill_info(self, skill: Skill):
        """打印技能信息"""
        print(f"\n{'='*60}")
        print(f"技能名称 (Skill Name): {skill.name}")
        print(f"分类 (Category): {skill.category}")
        print(f"描述 (Description): {skill.description}")
        print(f"\n实现 (Implementation):")
        print(skill.implementation)
        if skill.examples:
            print(f"\n示例 (Examples):")
            for i, example in enumerate(skill.examples, 1):
                print(f"  {i}. {example}")
        print(f"{'='*60}\n")


def main():
    """主函数，演示技能管理器的使用"""
    manager = SkillManager()
    
    # 加载所有技能
    count = manager.load_all_skills()
    print(f"已加载 {count} 个技能 (Loaded {count} skills)")
    
    # 列出所有分类
    categories = manager.list_categories()
    if categories:
        print(f"\n可用分类 (Available categories): {', '.join(categories)}")
    
    # 列出所有技能
    skills = manager.list_all_skills()
    if skills:
        print(f"\n所有技能 (All skills):")
        for skill in skills:
            print(f"  - {skill.name} ({skill.category}): {skill.description}")


if __name__ == '__main__':
    main()
