# AIcode Skills Project

一个用于管理和使用开发技能的工程 / A project for managing and using development skills

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

[中文](#中文) | [English](#english)

---

## 中文

### 📖 简介

AIcode Skills 是一个用于开发过程中管理各种技能的项目。它可以帮助你：

- 组织和管理开发技能
- 快速查找需要的技能
- 在 AIcode 开发过程中应用这些技能
- 扩展和自定义你自己的技能库

### ✨ 特性

- 🎯 **技能管理系统**: 完整的技能管理和组织系统
- 🔍 **快速搜索**: 按名称、描述、分类搜索技能
- 📂 **分类管理**: 按类别组织技能（代码质量、测试、架构等）
- 💡 **详细文档**: 每个技能包含实现方法、示例和工具推荐
- 🛠️ **易于扩展**: 支持添加自定义技能
- 🖥️ **命令行工具**: 提供便捷的CLI工具
- 📚 **Python API**: 可以在代码中集成使用

### 🚀 快速开始

#### 1. 克隆项目

```bash
git clone https://github.com/XL-Hello/AIcode.git
cd AIcode
```

#### 2. 查看可用技能

```bash
# 列出所有技能
python3 src/aicode_skills.py list

# 查看特定技能
python3 src/aicode_skills.py show code_review

# 搜索技能
python3 src/aicode_skills.py search 测试
```

#### 3. 运行示例

```bash
python3 examples/usage_examples.py
```

### 📁 项目结构

```
AIcode/
├── skills/              # 技能定义文件（JSON格式）
│   ├── code_review.json
│   ├── unit_testing.json
│   ├── api_design.json
│   └── ...
├── src/                 # 核心源代码
│   ├── skill_manager.py # 技能管理器
│   └── aicode_skills.py # 命令行工具
├── examples/            # 使用示例
│   └── usage_examples.py
├── docs/                # 文档
│   └── USAGE.md         # 详细使用指南
└── README.md            # 项目说明
```

### 🎓 已包含的技能

当前项目包含以下技能类别：

- **代码质量** (code_quality): 代码审查、重构
- **测试** (testing): 单元测试
- **架构** (architecture): API设计
- **故障排查** (troubleshooting): 调试
- **沟通** (communication): 文档编写

### 📖 详细文档

查看 [使用指南](docs/USAGE.md) 了解：
- 详细的安装说明
- 命令行工具使用方法
- Python API 使用示例
- 如何添加自定义技能
- 如何在项目中集成

### 💻 使用示例

#### 命令行使用

```bash
# 列出所有技能
python3 src/aicode_skills.py list

# 按分类列出
python3 src/aicode_skills.py list -c testing

# 查看技能详情
python3 src/aicode_skills.py show unit_testing

# 搜索技能
python3 src/aicode_skills.py search API
```

#### Python代码使用

```python
from skill_manager import SkillManager

# 初始化
manager = SkillManager()
manager.load_all_skills()

# 获取技能
skill = manager.get_skill('code_review')
print(skill.implementation)

# 搜索
results = manager.search_skills('测试')
```

### 🔧 添加自定义技能

创建 JSON 文件在 `skills/` 目录：

```json
{
  "name": "your_skill",
  "description": "技能描述",
  "category": "分类",
  "implementation": "实现方法...",
  "examples": ["示例1", "示例2"],
  "metadata": {
    "tools": ["工具1", "工具2"],
    "difficulty": "beginner"
  }
}
```

### 🤝 贡献

欢迎贡献！请随时提交 Pull Request。

### 📄 许可证

MIT License

---

## English

### 📖 Introduction

AIcode Skills is a project for managing various skills during the development process. It helps you:

- Organize and manage development skills
- Quickly find needed skills
- Apply these skills in AIcode development
- Extend and customize your own skill library

### ✨ Features

- 🎯 **Skills Management System**: Complete skill management and organization
- 🔍 **Quick Search**: Search skills by name, description, or category
- 📂 **Category Management**: Organize skills by categories (code quality, testing, architecture, etc.)
- 💡 **Detailed Documentation**: Each skill includes implementation methods, examples, and tool recommendations
- 🛠️ **Easy to Extend**: Support for adding custom skills
- 🖥️ **Command Line Tool**: Convenient CLI tool
- 📚 **Python API**: Can be integrated in code

### 🚀 Quick Start

#### 1. Clone the Project

```bash
git clone https://github.com/XL-Hello/AIcode.git
cd AIcode
```

#### 2. View Available Skills

```bash
# List all skills
python3 src/aicode_skills.py list

# Show specific skill
python3 src/aicode_skills.py show code_review

# Search skills
python3 src/aicode_skills.py search test
```

#### 3. Run Examples

```bash
python3 examples/usage_examples.py
```

### 📁 Project Structure

```
AIcode/
├── skills/              # Skill definition files (JSON format)
│   ├── code_review.json
│   ├── unit_testing.json
│   ├── api_design.json
│   └── ...
├── src/                 # Core source code
│   ├── skill_manager.py # Skill manager
│   └── aicode_skills.py # Command line tool
├── examples/            # Usage examples
│   └── usage_examples.py
├── docs/                # Documentation
│   └── USAGE.md         # Detailed usage guide
└── README.md            # Project description
```

### 🎓 Included Skills

Current project includes the following skill categories:

- **Code Quality** (code_quality): Code review, refactoring
- **Testing** (testing): Unit testing
- **Architecture** (architecture): API design
- **Troubleshooting** (troubleshooting): Debugging
- **Communication** (communication): Documentation writing

### 📖 Detailed Documentation

See [Usage Guide](docs/USAGE.md) for:
- Detailed installation instructions
- Command line tool usage
- Python API usage examples
- How to add custom skills
- How to integrate in projects

### 💻 Usage Examples

#### Command Line

```bash
# List all skills
python3 src/aicode_skills.py list

# List by category
python3 src/aicode_skills.py list -c testing

# Show skill details
python3 src/aicode_skills.py show unit_testing

# Search skills
python3 src/aicode_skills.py search API
```

#### Python Code

```python
from skill_manager import SkillManager

# Initialize
manager = SkillManager()
manager.load_all_skills()

# Get skill
skill = manager.get_skill('code_review')
print(skill.implementation)

# Search
results = manager.search_skills('test')
```

### 🔧 Add Custom Skills

Create a JSON file in `skills/` directory:

```json
{
  "name": "your_skill",
  "description": "Skill description",
  "category": "Category",
  "implementation": "Implementation...",
  "examples": ["Example 1", "Example 2"],
  "metadata": {
    "tools": ["Tool1", "Tool2"],
    "difficulty": "beginner"
  }
}
```

### 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

### 📄 License

MIT License
