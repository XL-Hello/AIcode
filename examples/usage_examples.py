#!/usr/bin/env python3
"""
使用AIcode Skills的示例代码
Examples of using AIcode Skills
"""

import sys
from pathlib import Path

# 添加src目录到Python路径
sys.path.insert(0, str(Path(__file__).parent.parent / 'src'))

from skill_manager import SkillManager


def example_1_list_all_skills():
    """示例1: 列出所有可用的技能"""
    print("=" * 60)
    print("示例1: 列出所有可用的技能")
    print("=" * 60)
    
    manager = SkillManager()
    manager.load_all_skills()
    
    skills = manager.list_all_skills()
    print(f"\n总共有 {len(skills)} 个技能:")
    for skill in skills:
        print(f"  - {skill.name}: {skill.description}")


def example_2_get_skills_by_category():
    """示例2: 按分类获取技能"""
    print("\n" + "=" * 60)
    print("示例2: 按分类获取技能")
    print("=" * 60)
    
    manager = SkillManager()
    manager.load_all_skills()
    
    # 获取所有分类
    categories = manager.list_categories()
    print(f"\n可用分类: {', '.join(categories)}")
    
    # 获取代码质量分类的技能
    if 'code_quality' in categories:
        skills = manager.get_skills_by_category('code_quality')
        print(f"\n代码质量 (code_quality) 相关技能:")
        for skill in skills:
            print(f"  - {skill.name}: {skill.description}")


def example_3_show_skill_details():
    """示例3: 显示特定技能的详细信息"""
    print("\n" + "=" * 60)
    print("示例3: 显示特定技能的详细信息")
    print("=" * 60)
    
    manager = SkillManager()
    manager.load_all_skills()
    
    # 获取并显示单元测试技能的详情
    skill = manager.get_skill('unit_testing')
    if skill:
        manager.print_skill_info(skill)


def example_4_search_skills():
    """示例4: 搜索技能"""
    print("\n" + "=" * 60)
    print("示例4: 搜索技能")
    print("=" * 60)
    
    manager = SkillManager()
    manager.load_all_skills()
    
    # 搜索包含"测试"的技能
    results = manager.search_skills('测试')
    print(f"\n搜索关键词 '测试' 的结果:")
    for skill in results:
        print(f"  - {skill.name}: {skill.description}")
    
    # 搜索包含"test"的技能
    results = manager.search_skills('test')
    print(f"\n搜索关键词 'test' 的结果:")
    for skill in results:
        print(f"  - {skill.name}: {skill.description}")


def example_5_use_skill_in_project():
    """示例5: 在项目中使用技能"""
    print("\n" + "=" * 60)
    print("示例5: 在项目中使用技能")
    print("=" * 60)
    
    manager = SkillManager()
    manager.load_all_skills()
    
    # 假设我们需要为一个项目进行代码审查
    skill = manager.get_skill('code_review')
    if skill:
        print(f"\n使用技能: {skill.name}")
        print(f"描述: {skill.description}")
        print(f"\n实现步骤:")
        print(skill.implementation)
        
        print(f"\n推荐工具:")
        if 'tools' in skill.metadata:
            for tool in skill.metadata['tools']:
                print(f"  - {tool}")
        
        print(f"\n预计时间: {skill.metadata.get('time_estimate', '未知')}")


def example_6_create_custom_skill():
    """示例6: 创建自定义技能"""
    print("\n" + "=" * 60)
    print("示例6: 创建自定义技能")
    print("=" * 60)
    
    from skill_manager import Skill
    
    manager = SkillManager()
    manager.load_all_skills()
    
    # 创建一个新的自定义技能
    custom_skill = Skill(
        name='performance_optimization',
        description='性能优化技能，分析和改进程序性能',
        category='optimization',
        implementation='性能优化流程：\n1. 使用性能分析工具找出瓶颈\n2. 分析算法复杂度\n3. 优化热点代码\n4. 减少不必要的计算和I/O\n5. 使用缓存策略\n6. 并行化处理',
        examples=[
            '使用cProfile分析Python代码性能',
            '优化数据库查询减少响应时间',
            '使用多线程/多进程提升处理速度',
            '实现缓存机制减少重复计算'
        ],
        metadata={
            'tools': ['cProfile', 'pyflame', 'perf', 'valgrind'],
            'difficulty': 'advanced',
            'time_estimate': '1-3小时'
        }
    )
    
    # 保存自定义技能
    manager.add_skill(custom_skill)
    print(f"\n创建了新技能: {custom_skill.name}")
    manager.print_skill_info(custom_skill)
    
    # 可以选择保存到文件
    # manager.save_skill(custom_skill)


if __name__ == '__main__':
    # 运行所有示例
    example_1_list_all_skills()
    example_2_get_skills_by_category()
    example_3_show_skill_details()
    example_4_search_skills()
    example_5_use_skill_in_project()
    example_6_create_custom_skill()
    
    print("\n" + "=" * 60)
    print("所有示例运行完成!")
    print("=" * 60)
