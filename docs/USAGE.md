# AIcode Skills 使用指南 / Usage Guide

[中文](#中文文档) | [English](#english-documentation)

---

## 中文文档

### 简介

AIcode Skills 是一个用于管理和使用开发技能的工程。它帮助开发者在使用 AIcode 开发过程中组织、查找和应用各种开发技能。

### 特性

- 🎯 **技能管理**: 组织和管理各种开发技能
- 🔍 **快速搜索**: 通过关键词快速找到需要的技能
- 📂 **分类系统**: 按类别组织技能，便于浏览
- 💡 **详细说明**: 每个技能包含实现方法、示例和元数据
- 🛠️ **可扩展**: 轻松添加自定义技能

### 安装

1. 克隆仓库:
```bash
git clone https://github.com/XL-Hello/AIcode.git
cd AIcode
```

2. 确保安装了 Python 3.6+:
```bash
python3 --version
```

### 快速开始

#### 使用命令行工具

1. **列出所有技能**:
```bash
python3 src/aicode_skills.py list
```

2. **查看特定技能的详情**:
```bash
python3 src/aicode_skills.py show unit_testing
```

3. **按分类列出技能**:
```bash
python3 src/aicode_skills.py list -c testing
```

4. **搜索技能**:
```bash
python3 src/aicode_skills.py search 测试
```

5. **列出所有分类**:
```bash
python3 src/aicode_skills.py categories
```

#### 在代码中使用

```python
from skill_manager import SkillManager

# 初始化管理器
manager = SkillManager()
manager.load_all_skills()

# 获取技能
skill = manager.get_skill('code_review')
print(skill.description)
print(skill.implementation)

# 搜索技能
results = manager.search_skills('测试')
for skill in results:
    print(f"{skill.name}: {skill.description}")
```

### 技能结构

每个技能包含以下信息:

- **name**: 技能名称（唯一标识）
- **description**: 技能描述
- **category**: 所属分类
- **implementation**: 实现方法和步骤
- **examples**: 使用示例
- **metadata**: 元数据（工具、难度、预计时间等）

### 已包含的技能

#### 代码质量 (code_quality)
- **code_review**: 代码审查
- **refactoring**: 代码重构

#### 测试 (testing)
- **unit_testing**: 单元测试

#### 架构 (architecture)
- **api_design**: API设计

#### 故障排查 (troubleshooting)
- **debugging**: 代码调试

#### 沟通 (communication)
- **documentation**: 文档编写

### 添加自定义技能

#### 方法1: 使用命令行工具

```bash
python3 src/aicode_skills.py create
```

按提示输入技能信息。

#### 方法2: 创建 JSON 文件

在 `skills/` 目录下创建 JSON 文件，格式如下:

```json
{
  "name": "your_skill_name",
  "description": "技能描述",
  "category": "category_name",
  "implementation": "实现步骤...",
  "examples": [
    "示例1",
    "示例2"
  ],
  "metadata": {
    "tools": ["tool1", "tool2"],
    "difficulty": "beginner|intermediate|advanced",
    "time_estimate": "预计时间"
  }
}
```

#### 方法3: 使用 Python API

```python
from skill_manager import SkillManager, Skill

manager = SkillManager()

# 创建新技能
skill = Skill(
    name='my_skill',
    description='我的自定义技能',
    category='custom',
    implementation='实现步骤...',
    examples=['示例1', '示例2']
)

# 保存技能
manager.save_skill(skill)
```

### 在项目中集成

您可以将 AIcode Skills 集成到您的项目中：

```python
# 在你的项目中
import sys
sys.path.append('/path/to/AIcode/src')

from skill_manager import SkillManager

# 使用技能管理器
manager = SkillManager('/path/to/AIcode/skills')
manager.load_all_skills()

# 根据需要获取和应用技能
```

### 示例

查看 `examples/usage_examples.py` 了解更多使用示例:

```bash
python3 examples/usage_examples.py
```

---

## English Documentation

### Introduction

AIcode Skills is a project for managing and using development skills. It helps developers organize, find, and apply various development skills when using AIcode.

### Features

- 🎯 **Skills Management**: Organize and manage various development skills
- 🔍 **Quick Search**: Find skills quickly by keywords
- 📂 **Category System**: Organize skills by categories for easy browsing
- 💡 **Detailed Information**: Each skill includes implementation methods, examples, and metadata
- 🛠️ **Extensible**: Easily add custom skills

### Installation

1. Clone the repository:
```bash
git clone https://github.com/XL-Hello/AIcode.git
cd AIcode
```

2. Ensure Python 3.6+ is installed:
```bash
python3 --version
```

### Quick Start

#### Using Command Line Tool

1. **List all skills**:
```bash
python3 src/aicode_skills.py list
```

2. **Show details of a specific skill**:
```bash
python3 src/aicode_skills.py show unit_testing
```

3. **List skills by category**:
```bash
python3 src/aicode_skills.py list -c testing
```

4. **Search for skills**:
```bash
python3 src/aicode_skills.py search test
```

5. **List all categories**:
```bash
python3 src/aicode_skills.py categories
```

#### Using in Code

```python
from skill_manager import SkillManager

# Initialize manager
manager = SkillManager()
manager.load_all_skills()

# Get a skill
skill = manager.get_skill('code_review')
print(skill.description)
print(skill.implementation)

# Search skills
results = manager.search_skills('test')
for skill in results:
    print(f"{skill.name}: {skill.description}")
```

### Skill Structure

Each skill contains the following information:

- **name**: Skill name (unique identifier)
- **description**: Skill description
- **category**: Category
- **implementation**: Implementation methods and steps
- **examples**: Usage examples
- **metadata**: Metadata (tools, difficulty, estimated time, etc.)

### Included Skills

#### Code Quality (code_quality)
- **code_review**: Code review
- **refactoring**: Code refactoring

#### Testing (testing)
- **unit_testing**: Unit testing

#### Architecture (architecture)
- **api_design**: API design

#### Troubleshooting (troubleshooting)
- **debugging**: Code debugging

#### Communication (communication)
- **documentation**: Documentation writing

### Adding Custom Skills

#### Method 1: Using Command Line Tool

```bash
python3 src/aicode_skills.py create
```

Follow the prompts to enter skill information.

#### Method 2: Create JSON File

Create a JSON file in the `skills/` directory with the following format:

```json
{
  "name": "your_skill_name",
  "description": "Skill description",
  "category": "category_name",
  "implementation": "Implementation steps...",
  "examples": [
    "Example 1",
    "Example 2"
  ],
  "metadata": {
    "tools": ["tool1", "tool2"],
    "difficulty": "beginner|intermediate|advanced",
    "time_estimate": "Estimated time"
  }
}
```

#### Method 3: Using Python API

```python
from skill_manager import SkillManager, Skill

manager = SkillManager()

# Create new skill
skill = Skill(
    name='my_skill',
    description='My custom skill',
    category='custom',
    implementation='Implementation steps...',
    examples=['Example 1', 'Example 2']
)

# Save skill
manager.save_skill(skill)
```

### Integrating in Your Project

You can integrate AIcode Skills into your project:

```python
# In your project
import sys
sys.path.append('/path/to/AIcode/src')

from skill_manager import SkillManager

# Use skill manager
manager = SkillManager('/path/to/AIcode/skills')
manager.load_all_skills()

# Get and apply skills as needed
```

### Examples

See `examples/usage_examples.py` for more usage examples:

```bash
python3 examples/usage_examples.py
```

---

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is open source and available under the MIT License.
