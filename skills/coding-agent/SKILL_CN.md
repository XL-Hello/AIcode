---
name: coding-agent
description: '通过后台进程委托编码任务给Codex、Claude Code或Pi代理。使用时机：(1) 构建/创建新功能或应用，(2) 审查PR（在临时目录中生成），(3) 重构大型代码库，(4) 需要文件探索的迭代编码。不适用于：简单的一行修复（直接编辑）、读取代码（使用读取工具）、聊天中的线程绑定ACP工具请求（例如在Discord线程中生成/运行Codex或Claude Code；使用sessions_spawn与runtime:"acp"），或在~/clawd工作区中的任何工作（永远不要在这里生成代理）。需要支持pty:true的bash工具。'
metadata:
  {
    "openclaw": { "emoji": "🧩", "requires": { "anyBins": ["claude", "codex", "opencode", "pi"] } },
  }
---

# 编码代理 (bash优先)

对所有编码代理工作使用 **bash**（可选后台模式）。简单有效。

## ⚠️ 需要PTY模式！

编码代理（Codex、Claude Code、Pi）是**交互式终端应用程序**，需要伪终端（PTY）才能正确工作。没有PTY，你会得到损坏的输出、缺失颜色，或代理可能挂起。

**运行编码代理时总是使用 `pty:true`**：

```bash
# ✅ 正确 - 带PTY
bash pty:true command:"codex exec 'Your prompt'"

# ❌ 错误 - 无PTY，代理可能中断
bash command:"codex exec 'Your prompt'"
```

### Bash工具参数

| 参数       | 类型    | 描述                                                                 |
| ---------- | ------- | -------------------------------------------------------------------- |
| `command`  | string  | 要运行的shell命令                                                    |
| `pty`      | boolean | **用于编码代理！** 为交互式CLI分配伪终端                            |
| `workdir`  | string  | 工作目录（代理只看到这个文件夹的上下文）                             |
| `background`| boolean | 在后台运行，返回sessionId用于监控                                 |
| `timeout`  | number  | 超时秒数（到期时杀死进程）                                          |
| `elevated` | boolean | 在主机上运行而不是沙箱（如果允许）                                   |

### 进程工具动作（用于后台会话）

| 动作       | 描述                                              |
| ---------- | ------------------------------------------------- |
| `list`     | 列出所有运行/最近会话                             |
| `poll`     | 检查会话是否仍在运行                              |
| `log`      | 获取会话输出（可选偏移/限制）                     |
| `write`    | 发送原始数据到stdin                               |
| `submit`   | 发送数据 + 新行（像输入并按Enter）                |
| `send-keys`| 发送键令牌或十六进制字节                          |
| `paste`    | 粘贴文本（可选括号模式）                          |
| `kill`     | 终止会话                                          |

---

## 快速开始：一次性任务

对于快速提示/聊天，创建一个临时git仓库并运行：

```bash
# 快速聊天（Codex需要git仓库！）
SCRATCH=$(mktemp -d) && cd $SCRATCH && git init && codex exec "Your prompt here"

# 或在真实项目中 - 带PTY！
bash pty:true workdir:~/Projects/myproject command:"codex exec 'Add error handling to the API calls'"
```

**为什么git init？** Codex拒绝在受信任的git目录外运行。为草稿工作创建临时仓库解决了这个问题。

---

## 模式：workdir + background + pty

对于更长任务，使用带PTY的后台模式：

```bash
# 在目标目录启动代理（带PTY！）
bash pty:true workdir:~/project background:true command:"codex exec --full-auto 'Build a snake game'"
# 返回sessionId用于跟踪

# 监控进度
process action:log sessionId:XXX

# 检查是否完成
process action:poll sessionId:XXX

# 发送输入（如果代理问问题）
process action:write sessionId:XXX data:"y"

# 用Enter提交（像输入"yes"并按Enter）
process action:submit sessionId:XXX data:"yes"

# 如果需要杀死
process action:kill sessionId:XXX
```

**为什么workdir重要：** 代理在聚焦目录中醒来，不会游荡读取无关文件（像你的soul.md 😅）。

---

## Codex CLI

**模型：** `gpt-5.2-codex` 是默认（在~/.codex/config.toml中设置）

### 标志

| 标志            | 效果                                             |
| --------------- | ------------------------------------------------ |
| `exec "prompt"` | 一次性执行，完成后退出                           |
| `--full-auto`   | 沙箱但在工作区自动批准                           |
| `--yolo`        | 无沙箱，无批准（最快，最危险）                   |

### 构建/创建

```bash
# 快速一次性（自动批准） - 记住PTY！
bash pty:true workdir:~/project command:"codex exec --full-auto 'Build a dark mode toggle'"

# 后台用于更长工作
bash pty:true workdir:~/project background:true command:"codex --yolo 'Refactor the auth module'"
```

### 审查PR

**⚠️ 关键：永远不要在OpenClaw自己的项目文件夹中审查PR！**
克隆到临时文件夹或使用git worktree。

```bash
# 克隆到临时用于安全审查
REVIEW_DIR=$(mktemp -d)
git clone https://github.com/user/repo.git $REVIEW_DIR
cd $REVIEW_DIR && gh pr checkout 130
bash pty:true workdir:$REVIEW_DIR command:"codex review --base origin/main"
# 之后清理：trash $REVIEW_DIR

# 或使用git worktree（保持main完整）
git worktree add /tmp/pr-130-review pr-130-branch
bash pty:true workdir:/tmp/pr-130-review command:"codex review --base main"
```

### 批量PR审查（并行军队！）

```bash
# 首先获取所有PR引用
git fetch origin '+refs/pull/*/head:refs/remotes/origin/pr/*'

# 部署军队 - 每个PR一个Codex（都带PTY！）
bash pty:true workdir:~/project background:true command:"codex exec 'Review PR #86. git diff origin/main...origin/pr/86'"
bash pty:true workdir:~/project background:true command:"codex exec 'Review PR #87. git diff origin/main...origin/pr/87'"

# 监控所有
process action:list

# 发布结果到GitHub
gh pr comment <PR#> --body "<review content>"
```

---

## Claude Code

```bash
# 带PTY用于正确终端输出
bash pty:true workdir:~/project command:"claude 'Your task'"

# 后台
bash pty:true workdir:~/project background:true command:"claude 'Your task'"
```

---

## OpenCode

```bash
bash pty:true workdir:~/project command:"opencode run 'Your task'"
```

---

## Pi编码代理

```bash
# 安装：npm install -g @mariozechner/pi-coding-agent
bash pty:true workdir:~/project command:"pi 'Your task'"

# 非交互模式（仍推荐PTY）
bash pty:true command:"pi -p 'Summarize src/'"

# 不同提供商/模型
bash pty:true command:"pi --provider openai --model gpt-4o-mini -p 'Your task'"
```

**注意：** Pi现在启用了Anthropic提示缓存（PR #584，2026年1月合并）！

---

## 使用git worktrees并行修复问题

为了并行修复多个问题，使用git worktrees：

```bash
# 1. 为每个问题创建worktrees
git worktree add -b fix/issue-78 /tmp/issue-78 main
git worktree add -b fix/issue-99 /tmp/issue-99 main

# 2. 在每个中启动Codex（后台 + PTY！）
bash pty:true workdir:/tmp/issue-78 background:true command:"pnpm install && codex --yolo 'Fix issue #78: <description>. Commit and push.'"
bash pty:true workdir:/tmp/issue-99 background:true command:"pnpm install && codex --yolo 'Fix issue #99 from the approved ticket summary. Implement only the in-scope edits and commit after review.'"

# 3. 监控进度
process action:list
process action:log sessionId:XXX

# 4. 修复后创建PR
cd /tmp/issue-78 && git push -u origin fix/issue-78
gh pr create --repo user/repo --head fix/issue-78 --title "fix: ..." --body "..."

# 5. 清理
git worktree remove /tmp/issue-78
git worktree remove /tmp/issue-99
```

---

## ⚠️ 规则

1. **总是使用pty:true** - 编码代理需要终端！
2. **尊重工具选择** - 如果用户要求Codex，使用Codex。
   - 编排器模式：不要自己手写补丁。
   - 如果代理失败/挂起，重新生成它或询问用户方向，但不要默默接管。
3. **耐心** - 不要因为“慢”而杀死会话
4. **用process:log监控** - 检查进度而不干扰
5. **--full-auto用于构建** - 自动批准更改
6. **vanilla用于审查** - 不需要特殊标志
7. **并行OK** - 为批量工作同时运行许多Codex进程
8. **永远不要在~/.openclaw/启动Codex** - 它会读取你的soul文档并对组织结构产生奇怪想法！
9. **永远不要在~/Projects/openclaw/检出分支** - 那是LIVE OpenClaw实例！

---

## 进度更新（关键）

当你在后台生成编码代理时，让用户保持循环。

- 启动时发送1条简短消息（什么在运行 + 哪里）。
- 然后只在有变化时再次更新：
  - 里程碑完成（构建完成，测试通过）
  - 代理问问题 / 需要输入
  - 你遇到错误或需要用户行动
  - 代理完成（包括改变了什么 + 哪里）
- 如果你杀死会话，立即说你杀死了它以及为什么。

这防止用户只看到“代理在回复前失败”而不知道发生了什么。

---

## 完成时自动通知

对于长时间运行的后台任务，在你的提示末尾附加唤醒触发器，这样OpenClaw在代理完成时立即得到通知（而不是等待下一次心跳）：

```
... 你的任务在这里。

完全完成后，运行这个命令通知我：
openclaw system event --text "Done: [brief summary of what was built]" --mode now
```

**示例：**

```bash
bash pty:true workdir:~/project background:true command:"codex --yolo exec 'Build a REST API for todos.

When completely finished, run: openclaw system event --text \"Done: Built todos REST API with CRUD endpoints\" --mode now'"
```

这触发立即唤醒事件——Skippy在几秒内得到ping，而不是10分钟。

---

## 学习（2026年1月）

- **PTY至关重要：** 编码代理是交互式终端应用。没有 `pty:true`，输出中断或代理挂起。
- **需要Git仓库：** Codex不会在git目录外运行。为草稿工作使用 `mktemp -d && git init`。
- **exec是你的朋友：** `codex exec "prompt"` 干净运行并退出 - 完美用于一次性。
- **submit vs write：** 使用 `submit` 发送输入 + Enter，使用 `write` 发送没有新行的原始数据。
- **Sass有效：** Codex对俏皮提示响应良好。问它写一个关于作为太空龙虾第二小提琴手的俳句，得到：_"Second chair, I code / Space lobster sets the tempo / Keys glow, I follow"_ 🦞