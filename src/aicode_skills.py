#!/usr/bin/env python3
"""
AIcode Skills CLI
命令行工具，用于管理和使用开发技能
"""

import argparse
import sys
from pathlib import Path

# 添加src目录到Python路径
sys.path.insert(0, str(Path(__file__).parent.parent / 'src'))

from skill_manager import SkillManager, Skill


def cmd_list(args, manager: SkillManager):
    """列出所有技能或特定分类的技能"""
    if args.category:
        skills = manager.get_skills_by_category(args.category)
        print(f"\n分类 '{args.category}' 中的技能:")
    else:
        skills = manager.list_all_skills()
        print("\n所有技能:")
    
    if not skills:
        print("  (无技能)")
        return
    
    for skill in sorted(skills, key=lambda s: s.name):
        print(f"  - {skill.name:20s} [{skill.category:15s}] {skill.description}")


def cmd_show(args, manager: SkillManager):
    """显示特定技能的详细信息"""
    skill = manager.get_skill(args.name)
    if not skill:
        print(f"错误: 未找到技能 '{args.name}'")
        sys.exit(1)
    
    manager.print_skill_info(skill)


def cmd_categories(args, manager: SkillManager):
    """列出所有技能分类"""
    categories = manager.list_categories()
    print("\n可用的技能分类:")
    for category in sorted(categories):
        count = len(manager.get_skills_by_category(category))
        print(f"  - {category:20s} ({count} 个技能)")


def cmd_search(args, manager: SkillManager):
    """搜索技能"""
    results = manager.search_skills(args.keyword)
    if not results:
        print(f"未找到包含 '{args.keyword}' 的技能")
        return
    
    print(f"\n搜索结果 (关键词: '{args.keyword}'):")
    for skill in results:
        print(f"  - {skill.name:20s} [{skill.category:15s}] {skill.description}")


def cmd_create(args, manager: SkillManager):
    """创建新技能"""
    # 交互式创建技能
    print("\n创建新技能:")
    name = input("技能名称 (Skill Name): ").strip()
    if not name:
        print("错误: 技能名称不能为空 (Error: Skill name cannot be empty)")
        sys.exit(1)
    
    if manager.get_skill(name):
        print(f"错误: 技能 '{name}' 已存在 (Error: Skill '{name}' already exists)")
        sys.exit(1)
    
    description = input("描述 (Description): ").strip()
    category = input("分类 (Category): ").strip()
    
    print("\n实现方法 (Implementation) - 输入多行，输入空行结束:")
    implementation_lines = []
    while True:
        line = input()
        if not line:
            break
        implementation_lines.append(line)
    implementation = '\n'.join(implementation_lines)
    
    print("\n示例 (Examples) - 每行一个，输入空行结束:")
    examples = []
    while True:
        line = input()
        if not line:
            break
        examples.append(line)
    
    skill = Skill(
        name=name,
        description=description,
        category=category,
        implementation=implementation,
        examples=examples
    )
    
    manager.save_skill(skill)
    print(f"\n✓ 技能 '{name}' 已创建并保存")


def main():
    parser = argparse.ArgumentParser(
        description='AIcode Skills Manager - 管理和使用开发技能',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
示例:
  %(prog)s list                    # 列出所有技能
  %(prog)s list -c testing         # 列出测试分类的技能
  %(prog)s show code_review        # 显示代码审查技能的详情
  %(prog)s categories              # 列出所有分类
  %(prog)s search test             # 搜索包含'test'的技能
  %(prog)s create                  # 创建新技能
        """
    )
    
    parser.add_argument('-d', '--skills-dir', 
                       help='技能目录路径 (默认: ../skills)')
    
    subparsers = parser.add_subparsers(dest='command', help='可用命令')
    
    # list 命令
    parser_list = subparsers.add_parser('list', help='列出技能')
    parser_list.add_argument('-c', '--category', help='按分类过滤')
    
    # show 命令
    parser_show = subparsers.add_parser('show', help='显示技能详情')
    parser_show.add_argument('name', help='技能名称')
    
    # categories 命令
    parser_categories = subparsers.add_parser('categories', 
                                             help='列出所有分类')
    
    # search 命令
    parser_search = subparsers.add_parser('search', help='搜索技能')
    parser_search.add_argument('keyword', help='搜索关键词')
    
    # create 命令
    parser_create = subparsers.add_parser('create', help='创建新技能')
    
    args = parser.parse_args()
    
    if not args.command:
        parser.print_help()
        sys.exit(1)
    
    # 初始化技能管理器
    manager = SkillManager(args.skills_dir)
    count = manager.load_all_skills()
    
    # 执行命令
    commands = {
        'list': cmd_list,
        'show': cmd_show,
        'categories': cmd_categories,
        'search': cmd_search,
        'create': cmd_create,
    }
    
    if args.command in commands:
        commands[args.command](args, manager)
    else:
        parser.print_help()
        sys.exit(1)


if __name__ == '__main__':
    main()
