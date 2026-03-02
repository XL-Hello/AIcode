# Git Commit Viewer 技能使用说明

## 功能概述

该技能用于根据Git commit号查询代码变更，将结果输出到Markdown文档中，便于代码审查和变更追踪。

## 目录结构

```
git-commit-viewer/
├── SKILL.md                    # 技能定义文件
├── scripts/                    # 脚本目录
│   ├── view_commit.py         # Python版本脚本（推荐）
│   └── view_commit.sh         # Bash版本脚本
├── temp/                       # 输出文件目录
│   └── <commit_hash>.md       # 生成的commit信息文件
└── README.md                  # 本说明文件
```

## 使用方法

### 方法一：使用Python脚本（推荐）

```bash
python3 scripts/view_commit.py <仓库绝对路径> <commit号> [输出目录]
```

**示例：**
```bash
python3 scripts/view_commit.py /home/user/myproject abc123def
```

### 方法二：使用Bash脚本

```bash
bash scripts/view_commit.sh <仓库绝对路径> <commit号> [输出目录]
```

**示例：**
```bash
bash scripts/view_commit.sh /home/user/myproject abc123def
```

### 参数说明

1. **仓库绝对路径**（必需）
   - Git仓库的完整路径
   - 必须包含 `.git` 目录

2. **commit号**（必需）
   - Git commit的哈希值
   - 支持短哈希或完整哈希

3. **输出目录**（可选）
   - 指定输出文件的保存位置
   - 默认为技能目录下的 `temp/` 文件夹

## 输出文件

### 文件位置
- 默认位置：`skills/git-commit-viewer/temp/<commit号>.md`
- 自定义位置：由 `输出目录` 参数指定

### 文件格式

生成的Markdown文件包含：

```markdown
# Commit: abc123def

```diff
commit abc123def...
Author: 作者名 <邮箱>
Date:   提交日期

    提交信息

diff --git a/文件路径 b/文件路径
...
```
```

### 文件内容
- Commit基本信息（作者、日期、提交信息）
- 完整的diff内容
- 使用 `diff` 代码块格式，支持语法高亮

## 使用示例

### 示例1：查看指定commit
```bash
# 查看commit e0e2f8d
python3 scripts/view_commit.py /home/xl/dreame/AIcode e0e2f8d

# 输出：/home/xl/dreame/AIcode/skills/git-commit-viewer/temp/e0e2f8d.md
```

### 示例2：自定义输出目录
```bash
# 将输出保存到指定目录
python3 scripts/view_commit.py /home/user/backend abc123 /tmp/commits

# 输出：/tmp/commits/abc123.md
```

### 示例3：批量查看多个commit
```bash
# 查看最近的5个commit
cd /home/user/myproject
git log --oneline -5 | cut -d' ' -f1 | while read hash; do
    python3 /path/to/scripts/view_commit.py $(pwd) $hash
done
```

## 错误处理

脚本会自动处理以下错误：
- **路径不存在**：提示"路径不存在"
- **不是Git仓库**：提示"不是Git仓库"
- **commit不存在**：返回Git错误信息
- **权限问题**：提示无法写入输出目录

## 技能打包文件

技能已打包为：`/home/xl/dreame/AIcode/git-commit-viewer.zip`

包含内容：
- SKILL.md
- scripts/view_commit.py
- scripts/view_commit.sh

## 注意事项

1. 确保Python 3环境可用（使用Python脚本时）
2. 确保Bash环境可用（使用Bash脚本时）
3. 输出目录会自动创建，无需手动创建
4. `temp/` 目录下的文件可以手动清理以节省空间
5. 每次执行会覆盖同名文件

## 适用场景

- 代码审查时查看特定commit的变更
- 提取commit信息用于文档编写
- 分析代码变更历史
- 生成commit变更报告
