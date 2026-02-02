# 技能模板 / Skill Template

## 创建新技能 / Creating a New Skill

### 方法1：使用CLI工具 / Method 1: Using CLI Tool

```bash
python3 src/aicode_skills.py create
```

### 方法2：复制此模板 / Method 2: Copy This Template

将此文件复制到 `skills/` 目录并重命名为 `your_skill_name.json`

Copy this file to the `skills/` directory and rename it to `your_skill_name.json`

---

## JSON模板 / JSON Template

```json
{
  "name": "skill_name_here",
  "description": "简短描述这个技能的用途（中英文皆可）/ Brief description of the skill (Chinese or English)",
  "category": "category_name",
  "implementation": "详细说明如何实现这个技能的步骤：\n1. 第一步\n2. 第二步\n3. 第三步\n...",
  "examples": [
    "示例1：具体使用场景或例子",
    "示例2：另一个使用场景",
    "示例3：更多例子"
  ],
  "metadata": {
    "tools": ["tool1", "tool2", "tool3"],
    "difficulty": "beginner|intermediate|advanced",
    "time_estimate": "预计完成时间",
    "languages": ["python", "javascript", "any"]
  }
}
```

---

## 字段说明 / Field Descriptions

### name (必需 / Required)
- 技能的唯一标识符 / Unique identifier for the skill
- 使用小写字母和下划线 / Use lowercase letters and underscores
- 示例 / Examples: `code_review`, `unit_testing`, `api_design`

### description (必需 / Required)
- 技能的简短描述 / Brief description of the skill
- 一到两句话说明技能的用途 / One to two sentences explaining the purpose
- 示例 / Example: "代码审查技能，帮助检查代码质量、潜在bug和改进建议"

### category (必需 / Required)
- 技能所属的分类 / Category the skill belongs to
- 常用分类 / Common categories:
  - `code_quality` - 代码质量 / Code quality
  - `testing` - 测试 / Testing
  - `architecture` - 架构 / Architecture
  - `security` - 安全 / Security
  - `devops` - 运维 / DevOps
  - `development` - 开发 / Development
  - `troubleshooting` - 故障排查 / Troubleshooting
  - `communication` - 沟通 / Communication
  - `version_control` - 版本控制 / Version control

### implementation (必需 / Required)
- 详细的实现步骤和方法 / Detailed implementation steps and methods
- 可以使用 `\n` 换行 / Use `\n` for line breaks
- 建议使用编号列表 / Numbered lists recommended
- 示例 / Example:
  ```
  "implementation": "步骤：\n1. 第一步做什么\n2. 第二步做什么\n3. 第三步做什么"
  ```

### examples (可选 / Optional)
- 使用示例列表 / List of usage examples
- 每个示例应该具体且实用 / Each example should be specific and practical
- 示例 / Examples:
  ```json
  "examples": [
    "使用pytest为Python函数编写测试",
    "使用JUnit为Java方法编写测试"
  ]
  ```

### metadata (可选 / Optional)
附加的元数据信息 / Additional metadata information

#### tools (可选 / Optional)
- 推荐使用的工具列表 / List of recommended tools
- 示例 / Example: `["pytest", "junit", "jest"]`

#### difficulty (可选 / Optional)
- 技能难度级别 / Skill difficulty level
- 可选值 / Options: `"beginner"`, `"intermediate"`, `"advanced"`

#### time_estimate (可选 / Optional)
- 预计完成时间 / Estimated completion time
- 示例 / Example: `"30分钟-1小时"` 或 `"30 minutes - 1 hour"`

#### languages (可选 / Optional)
- 适用的编程语言 / Applicable programming languages
- 示例 / Example: `["python", "javascript", "java"]`
- 如果适用于所有语言 / If applicable to all languages: `["any"]`

---

## 完整示例 / Complete Example

```json
{
  "name": "code_optimization",
  "description": "代码优化技能，提升代码性能和效率",
  "category": "code_quality",
  "implementation": "代码优化流程：\n1. 使用性能分析工具识别瓶颈\n2. 分析算法时间和空间复杂度\n3. 优化数据结构选择\n4. 减少不必要的计算\n5. 利用缓存和记忆化\n6. 并行化可并行的操作\n7. 验证优化效果",
  "examples": [
    "将O(n²)算法优化为O(n log n)",
    "使用缓存避免重复计算",
    "优化数据库查询减少N+1问题",
    "使用异步I/O提升并发性能"
  ],
  "metadata": {
    "tools": ["cProfile", "line_profiler", "py-spy", "perf"],
    "difficulty": "intermediate",
    "time_estimate": "1-2小时",
    "languages": ["python", "javascript", "java", "c++"]
  }
}
```

---

## 验证技能 / Validate Skill

创建技能文件后，验证它是否正确加载：

After creating the skill file, validate it loads correctly:

```bash
# 列出所有技能（应该包含你的新技能）
# List all skills (should include your new skill)
python3 src/aicode_skills.py list

# 查看你的技能详情
# View your skill details
python3 src/aicode_skills.py show your_skill_name
```

---

## 贡献技能 / Contributing Skills

如果你创建了有用的技能，欢迎贡献到项目中：

If you created useful skills, contributions are welcome:

1. Fork 这个仓库 / Fork this repository
2. 添加你的技能文件 / Add your skill file
3. 提交 Pull Request / Submit a Pull Request
4. 在PR中说明技能的用途 / Describe the skill's purpose in the PR

---

## 技能命名规范 / Skill Naming Conventions

- 使用小写字母 / Use lowercase letters
- 使用下划线分隔单词 / Use underscores to separate words
- 保持简洁但有描述性 / Keep it concise but descriptive
- 避免使用特殊字符 / Avoid special characters

✅ 好的命名 / Good names:
- `code_review`
- `unit_testing`
- `api_design`
- `security_audit`

❌ 避免的命名 / Names to avoid:
- `CodeReview` (使用小写 / use lowercase)
- `code-review` (使用下划线 / use underscores)
- `CR` (太简短 / too short)
- `code_review_skill_for_python` (太长 / too long)
