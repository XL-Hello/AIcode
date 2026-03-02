---
name: git-commit-viewer
description: 当查询特定提交哈希的 Git 提交更改时使用此技能。当用户请求查看、提取或分析特定提交的代码更改时使用。触发包括如"显示提交 abc123"、"查看提交更改"、"获取提交详情"或"提取提交信息"等请求。
---

# Git 提交查看器

## 概述

通过提交哈希查询和提取 Git 提交更改，将详细的代码差异输出到 Markdown 文件中，便于审查和分析。

## 何时使用此技能

当以下情况时使用此技能：
- 用户提供提交哈希并希望查看更改
- 用户要求分析特定提交修改
- 用户需要提取提交信息用于文档或审查
- 用户请求以结构化格式获取提交详情

## 工作流程

### 步骤 1：获取所需信息

在执行提交查看器之前，从用户处获取以下信息：

1. **Git 仓库路径**：Git 仓库的绝对路径
   - 如果未提供，请用户提供项目目录
   - 验证路径存在且包含 `.git` 目录

2. **提交哈希**：要查询的提交标识符
   - 接受短哈希或完整哈希
   - 验证提交在仓库中存在

### 步骤 2：执行提交查看器

使用提供的脚本提取提交信息：

**选项 A：Python 脚本（推荐）**
```bash
python3 scripts/view_commit.py <repo_path> <commit_hash> [output_dir]
```

**选项 B：Bash 脚本**
```bash
bash scripts/view_commit.sh <repo_path> <commit_hash> [output_dir]
```

**参数：**
- `repo_path`：Git 仓库的绝对路径
- `commit_hash`：要查询的提交哈希
- `output_dir`：（可选）输出目录路径。默认为技能目录中的 `temp/` 文件夹

**示例：**
```bash
python3 scripts/view_commit.py /home/user/myproject abc123def
```

### 步骤 3：检索并返回输出文件

执行后：
1. 脚本在 `temp/<commit_hash>.md` 创建 Markdown 文件
2. 读取生成的文件以向用户显示提交更改
3. 返回文件的绝对路径给用户

**输出文件格式：**
```markdown
# 提交：abc123def

```diff
commit abc123def...
Author: ...
Date: ...

diff --git a/...
...
```
```

## 输出位置

- **默认位置**：`skills/git-commit-viewer/temp/<commit_hash>.md`
- **自定义位置**：通过 `output_dir` 参数指定
- 如果不存在，`temp/` 目录会自动创建

## 使用示例

**示例 1：基本用法**
```
用户：显示项目 /home/user/myapp 中提交 abc123 的内容
→ 执行：python3 scripts/view_commit.py /home/user/myapp abc123
→ 返回：/home/xl/dreame/AIcode/skills/git-commit-viewer/temp/abc123.md
```

**示例 2：自定义输出目录**
```
用户：从 /home/user/backend 提取提交 def456 并保存到 /tmp/commits
→ 执行：python3 scripts/view_commit.py /home/user/backend def456 /tmp/commits
→ 返回：/tmp/commits/def456.md
```

**示例 3：查看最近提交**
```
用户：/home/user/frontend 的最后一次提交有什么更改？
→ 执行：cd /home/user/frontend && git log -1 --oneline
→ 然后：python3 scripts/view_commit.py /home/user/frontend <hash>
```

## 资源

### scripts/

- `view_commit.py`：用于提取提交信息的 Python 脚本，具有错误处理
- `view_commit.sh`：Bash 替代方案，用于没有 Python 的环境

### temp/

自动生成的目录，包含输出 Markdown 文件：
- 文件命名格式为 `<commit_hash>.md`
- 每个文件包含完整的提交差异，以 Markdown 格式
- 可以安全删除旧文件以节省空间

## 错误处理

脚本处理常见错误：
- **无效仓库路径**：如果路径不存在或不是 Git 仓库，则报告
- **无效提交哈希**：如果提交不存在，则返回 Git 错误消息
- **权限问题**：如果无法写入输出目录，则报告

## 注意事项

- 提交输出包括带有语法高亮的完整差异信息
- Markdown 格式使用 `diff` 代码块以正确渲染
- 在同一会话中可以提取多个提交到单独的文件