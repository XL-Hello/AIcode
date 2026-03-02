---
name: using-git-worktrees
description: 当开始需要与当前工作区隔离的功能工作或在执行实施计划之前使用 - 创建具有智能目录选择和安全验证的隔离git worktrees
---

# 使用Git Worktrees

## 概述

Git worktrees 创建共享同一仓库的隔离工作区，允许同时在多个分支上工作而无需切换。

**核心原则：** 系统目录选择 + 安全验证 = 可靠隔离。

**在开始宣布：** “我正在使用using-git-worktrees技能来设置隔离工作区。”

## 目录选择过程

遵循这个优先顺序：

### 1. 检查现有目录

```bash
# 按优先顺序检查
ls -d .worktrees 2>/dev/null     # 首选（隐藏）
ls -d worktrees 2>/dev/null      # 替代
```

**如果找到：** 使用那个目录。如果两者都存在，`.worktrees` 赢。

### 2. 检查CLAUDE.md

```bash
grep -i "worktree.*director" CLAUDE.md 2>/dev/null
```

**如果指定偏好：** 使用它而不询问。

### 3. 询问用户

如果没有目录存在且没有CLAUDE.md偏好：

```
没有找到worktree目录。我应该在哪里创建worktrees？

1. .worktrees/ (项目本地，隐藏)
2. ~/.config/superpowers/worktrees/<project-name>/ (全局位置)

你更喜欢哪个？
```

## 安全验证

### 对于项目本地目录（.worktrees 或 worktrees）

**必须在创建worktree之前验证目录被忽略：**

```bash
# 检查目录是否被忽略（尊重本地、全局和系统gitignore）
git check-ignore -q .worktrees 2>/dev/null || git check-ignore -q worktrees 2>/dev/null
```

**如果没有被忽略：**

根据Jesse的规则“立即修复损坏的东西”：
1. 添加适当行到.gitignore
2. 提交改变
3. 继续worktree创建

**为什么关键：** 防止意外提交worktree内容到仓库。

### 对于全局目录（~/.config/superpowers/worktrees）

不需要.gitignore验证 - 完全在项目外。

## 创建步骤

### 1. 检测项目名称

```bash
project=$(basename "$(git rev-parse --show-toplevel)")
```

### 2. 创建Worktree

```bash
# 确定完整路径
case $LOCATION in
  .worktrees|worktrees)
    path="$LOCATION/$BRANCH_NAME"
    ;;
  ~/.config/superpowers/worktrees/*)
    path="~/.config/superpowers/worktrees/$project/$BRANCH_NAME"
    ;;
esac

# 用新分支创建worktree
git worktree add "$path" -b "$BRANCH_NAME"
cd "$path"
```

### 3. 运行项目设置

自动检测并运行适当设置：

```bash
# Node.js
if [ -f package.json ]; then npm install; fi

# Rust
if [ -f Cargo.toml ]; then cargo build; fi

# Python
if [ -f requirements.txt ]; then pip install -r requirements.txt; fi
if [ -f pyproject.toml ]; then poetry install; fi

# Go
if [ -f go.mod ]; then go mod download; fi
```

### 4. 验证干净基准

运行测试确保worktree从干净开始：

```bash
# 示例 - 使用项目适当命令
npm test
cargo test
pytest
go test ./...
```

**如果测试失败：** 报告失败，询问是否继续或调查。

**如果测试通过：** 报告就绪。

### 5. 报告位置

```
Worktree 就绪于 <full-path>
测试通过 (<N> 测试, 0 失败)
准备实施 <feature-name>
```

## 快速参考

| 情况 | 行动 |
|-----------|--------|
| `.worktrees/` 存在 | 使用它（验证忽略） |
| `worktrees/` 存在 | 使用它（验证忽略） |
| 两者都存在 | 使用 `.worktrees/` |
| 都不存在 | 检查CLAUDE.md → 询问用户 |
| 目录未忽略 | 添加到.gitignore + 提交 |
| 基准期间测试失败 | 报告失败 + 询问 |
| 没有package.json/Cargo.toml | 跳过依赖安装 |

## 常见错误

### 跳过忽略验证

- **问题：** Worktree内容被跟踪，污染git状态
- **修复：** 在创建项目本地worktree之前总是使用 `git check-ignore`

### 假设目录位置

- **问题：** 创建不一致，违反项目约定
- **修复：** 遵循优先：现有 > CLAUDE.md > 询问

### 继续失败测试

- **问题：** 不能区分新bug和预存在问题
- **修复：** 报告失败，获取明确许可继续

### 硬编码设置命令

- **问题：** 在使用不同工具的项目上中断
- **修复：** 从项目文件自动检测（package.json等）

## 示例工作流程

```
你：我正在使用using-git-worktrees技能来设置隔离工作区。

[检查 .worktrees/ - 存在]
[验证忽略 - git check-ignore 确认 .worktrees/ 被忽略]
[创建worktree: git worktree add .worktrees/auth -b feature/auth]
[运行 npm install]
[运行 npm test - 47 通过]

Worktree 就绪于 /Users/jesse/myproject/.worktrees/auth
测试通过 (47 测试, 0 失败)
准备实施 auth 功能
```

## 红旗

**永远不要：**
- 在验证它被忽略之前创建worktree（项目本地）
- 跳过基准测试验证
- 在没有询问的情况下继续失败测试
- 当模糊时假设目录位置
- 跳过CLAUDE.md检查

**总是：**
- 遵循目录优先：现有 > CLAUDE.md > 询问
- 为项目本地验证目录被忽略
- 自动检测并运行项目设置
- 验证干净测试基准

## 集成

**被调用：**
- **brainstorming** (阶段4) - 当设计被批准且实施跟随时必需
- **subagent-driven-development** - 在执行任何任务之前必需
- **executing-plans** - 在执行任何任务之前必需
- 任何需要隔离工作区的技能

**与配对：**
- **finishing-a-development-branch** - 当工作完成后清理必需