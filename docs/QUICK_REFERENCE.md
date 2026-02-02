# AIcode Skills 快速参考 / Quick Reference

## 命令行快速参考 / CLI Quick Reference

### 基本命令 / Basic Commands

```bash
# 列出所有技能 / List all skills
python3 src/aicode_skills.py list

# 按分类列出技能 / List skills by category
python3 src/aicode_skills.py list -c testing

# 查看技能详情 / Show skill details
python3 src/aicode_skills.py show code_review

# 列出所有分类 / List all categories
python3 src/aicode_skills.py categories

# 搜索技能 / Search skills
python3 src/aicode_skills.py search 测试

# 创建新技能 / Create new skill
python3 src/aicode_skills.py create

# 查看帮助 / Show help
python3 src/aicode_skills.py --help
```

## Python API 快速参考 / Python API Quick Reference

### 基本使用 / Basic Usage

```python
from skill_manager import SkillManager, Skill

# 初始化管理器 / Initialize manager
manager = SkillManager()
count = manager.load_all_skills()
print(f"已加载 {count} 个技能")

# 获取技能 / Get a skill
skill = manager.get_skill('code_review')
if skill:
    print(skill.name)
    print(skill.description)
    print(skill.implementation)

# 列出所有技能 / List all skills
all_skills = manager.list_all_skills()
for skill in all_skills:
    print(f"{skill.name}: {skill.description}")

# 按分类获取 / Get by category
testing_skills = manager.get_skills_by_category('testing')

# 列出分类 / List categories
categories = manager.list_categories()

# 搜索技能 / Search skills
results = manager.search_skills('API')

# 打印技能信息 / Print skill info
manager.print_skill_info(skill)
```

### 创建技能 / Creating Skills

```python
from skill_manager import Skill, SkillManager

# 创建技能对象 / Create skill object
skill = Skill(
    name='my_skill',
    description='我的自定义技能',
    category='custom',
    implementation='实现步骤...',
    examples=['示例1', '示例2'],
    metadata={
        'tools': ['tool1'],
        'difficulty': 'beginner'
    }
)

# 添加到管理器 / Add to manager
manager = SkillManager()
manager.add_skill(skill)

# 保存到文件 / Save to file
manager.save_skill(skill)
```

## 技能结构 / Skill Structure

```json
{
  "name": "skill_name",
  "description": "技能描述",
  "category": "分类",
  "implementation": "实现方法",
  "examples": ["示例1", "示例2"],
  "metadata": {
    "tools": ["工具列表"],
    "difficulty": "难度级别",
    "time_estimate": "预计时间",
    "languages": ["适用语言"]
  }
}
```

## 常用分类 / Common Categories

| 分类 Category | 说明 Description |
|---------------|------------------|
| `code_quality` | 代码质量相关 / Code quality |
| `testing` | 测试相关 / Testing |
| `architecture` | 架构设计 / Architecture |
| `security` | 安全相关 / Security |
| `devops` | 运维部署 / DevOps |
| `development` | 开发实现 / Development |
| `troubleshooting` | 故障排查 / Troubleshooting |
| `communication` | 文档沟通 / Communication |
| `version_control` | 版本控制 / Version control |

## 当前可用技能 / Currently Available Skills

### 代码质量 / Code Quality
- `code_review` - 代码审查
- `refactoring` - 代码重构

### 测试 / Testing
- `unit_testing` - 单元测试

### 架构 / Architecture
- `api_design` - API设计
- `database_design` - 数据库设计
- `microservices_design` - 微服务架构

### 安全 / Security
- `security_audit` - 安全审计

### DevOps
- `ci_cd_setup` - CI/CD配置

### 开发 / Development
- `frontend_development` - 前端开发

### 故障排查 / Troubleshooting
- `debugging` - 代码调试

### 沟通 / Communication
- `documentation` - 文档编写

### 版本控制 / Version Control
- `git_workflow` - Git工作流

## 常见用例 / Common Use Cases

### 1. 项目开始前的技能准备
```bash
# 查看项目需要的技能
python3 src/aicode_skills.py list -c architecture
python3 src/aicode_skills.py show api_design
python3 src/aicode_skills.py show database_design
```

### 2. 代码审查流程
```bash
# 获取代码审查指南
python3 src/aicode_skills.py show code_review
```

### 3. 设置CI/CD
```bash
# 查看CI/CD配置步骤
python3 src/aicode_skills.py show ci_cd_setup
```

### 4. 安全检查
```bash
# 查看安全审计流程
python3 src/aicode_skills.py show security_audit
```

## 集成到项目 / Integrating into Projects

### 在Python项目中使用
```python
import sys
sys.path.append('/path/to/AIcode/src')

from skill_manager import SkillManager

manager = SkillManager('/path/to/AIcode/skills')
manager.load_all_skills()

# 使用技能
skill = manager.get_skill('unit_testing')
print(f"执行 {skill.name}:")
print(skill.implementation)
```

### 在Shell脚本中使用
```bash
#!/bin/bash

# 获取技能列表
SKILLS=$(python3 /path/to/AIcode/src/aicode_skills.py list)
echo "$SKILLS"

# 查看特定技能
python3 /path/to/AIcode/src/aicode_skills.py show code_review
```

## 故障排查 / Troubleshooting

### 找不到技能
```bash
# 确认技能文件存在
ls skills/

# 重新加载技能
python3 src/skill_manager.py
```

### Python路径问题
```python
# 确保添加了正确的路径
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent / 'src'))
```

## 更多资源 / More Resources

- [详细使用指南](USAGE.md) - 完整的使用文档
- [技能模板](SKILL_TEMPLATE.md) - 创建新技能的模板
- [示例代码](../examples/usage_examples.py) - Python使用示例
