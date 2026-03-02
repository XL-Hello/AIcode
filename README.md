# AIcode
一个嵌入式AICode的skills工程。

使用方法：
- 将目标项目放在 [projects](projects) 下。
- 然后利用 [skills](skills) 下的方法进行相关的AI操作。

## 目录
- [projects](projects): 存放待处理的工程项目。
- [skills](skills): 存放各种 AI 技能及其执行规范。

## Skills 概述

下面的内容会持续更新，目标是让你在“几秒内选对技能”。

### 标注说明（必须/推荐/可选）

- **MUST（按场景必须）**：只要任务命中该场景，就必须先用该技能（或遵循其硬性流程）。
- **RECOMMENDED（强烈推荐）**：不是硬性，但能显著降低返工/风险。
- **OPTIONAL（按需）**：工具箱型能力，视团队习惯/目标选择。

### 0) 起手式：先选技能，再行动（强制）

- **using-superpowers**（MUST）：任何回应/行动前先做“技能检查”，不要先问澄清问题再说。
  - 入口：
    - [skills/using-superpowers/SKILL.md](skills/using-superpowers/SKILL.md)
    - [skills/using-superpowers/SKILL_CN.md](skills/using-superpowers/SKILL_CN.md)

### 1) 流程与协作（先对齐，再动手）

- **plan**（RECOMMENDED）：复杂任务的迭代式规划（收集信息→草案→澄清→批准→实施）。
  - 入口：[skills/plan/SKILL.md](skills/plan/SKILL.md) / [skills/plan/SKILL_CN.md](skills/plan/SKILL_CN.md)
- **architect**（RECOMMENDED）：做方案对比、取舍、风险与分阶段落地计划（不直接改代码）。
  - 入口：[skills/architect/SKILL.md](skills/architect/SKILL.md) / [skills/architect/SKILL_CN.md](skills/architect/SKILL_CN.md)
- **software-architecture**（RECOMMENDED）：用 Clean Architecture / DDD 的“日常规则”约束结构与可维护性。
  - 入口：[skills/software-architecture/SKILL.md](skills/software-architecture/SKILL.md)
- **ship-learn-next**（RECOMMENDED）：把学习材料转成可交付的 Rep（ship→reflect→next），适合训练式推进。
  - 入口：[skills/ship-learn-next/SKILL.md](skills/ship-learn-next/SKILL.md) / [skills/ship-learn-next/SKILL_CN.md](skills/ship-learn-next/SKILL_CN.md)
- **prompt-engineering**（RECOMMENDED）：当你在写“提示/指令/模板/技能描述”本身时使用。
  - 入口：[skills/prompt-engineering/SKILL.md](skills/prompt-engineering/SKILL.md) / [skills/prompt-engineering/SKILL_CN.md](skills/prompt-engineering/SKILL_CN.md)
- **skill-creator**（RECOMMENDED）：当你要“创建/改进一个技能”并希望用评测闭环迭代时。
  - 入口：[skills/skill-creator/SKILL.md](skills/skill-creator/SKILL.md) / [skills/skill-creator/SKILL_CN.md](skills/skill-creator/SKILL_CN.md)

### 2) 发现与实现（读/写/代理化）

- **explorer**（RECOMMENDED）：只做定位与脉络梳理（不改代码），适合快速找入口、调用链、配置点。
  - 入口：[skills/explorer/SKILL.md](skills/explorer/SKILL.md) / [skills/explorer/SKILL_CN.md](skills/explorer/SKILL_CN.md)
- **coder**（RECOMMENDED）：真正落地实现/修复/重构（会改文件、跑命令、做验证）。
  - 入口：[skills/coder/SKILL.md](skills/coder/SKILL.md) / [skills/coder/SKILL_CN.md](skills/coder/SKILL_CN.md)
- **coding-agent**（RECOMMENDED）：把大任务委托给交互式终端编码代理（Codex/Claude Code/Pi），支持后台会话+PTY。
  - 入口：[skills/coding-agent/SKILL.md](skills/coding-agent/SKILL.md) / [skills/coding-agent/SKILL_CN.md](skills/coding-agent/SKILL_CN.md)
- **using-git-worktrees**（MUST，按场景）：需要隔离工作区/并行分支/执行实施计划前，先用 worktree 建隔离环境并做 ignore 与基线测试校验。
  - 入口：[skills/using-git-worktrees/SKILL.md](skills/using-git-worktrees/SKILL.md) / [skills/using-git-worktrees/SKILL_CN.md](skills/using-git-worktrees/SKILL_CN.md)
- **shell-scripting**（RECOMMENDED）：写 bash/zsh 自动化脚本与CLI（健壮性、参数解析、trap、严格模式）。
  - 入口：[skills/shell-scripting/SKILL.md](skills/shell-scripting/SKILL.md) / [skills/shell-scripting/SKILL_CN.md](skills/shell-scripting/SKILL_CN.md)

### 3) 领域/项目特化（命中就优先）

- **awtk-dev**（MUST，按场景）：改 AWTK 项目代码时遵循工程约束（命名/风格/内存/编译验证）。
  - 入口：[skills/awtk-dev/SKILL.md](skills/awtk-dev/SKILL.md)
- **mcp-builder**（MUST，按场景）：构建 MCP Server（工具Schema/传输/评测/最佳实践）。
  - 入口：[skills/mcp-builder/SKILL.md](skills/mcp-builder/SKILL.md) / [skills/mcp-builder/SKILL_CN.md](skills/mcp-builder/SKILL_CN.md)
- **frontend-design**（RECOMMENDED）：当目标是高质量、非“AI通用模板感”的前端UI/视觉方向时。
  - 入口：[skills/frontend-design/SKILL.md](skills/frontend-design/SKILL.md) / [skills/frontend-design/SKILL_CN.md](skills/frontend-design/SKILL_CN.md)

### 4) 评审与质量（减少缺陷与返工）

- **test-driven-development**（MUST，按场景）：实现功能/修Bug/重构时优先测试先行（红-绿-重构）。
  - 入口：[skills/test-driven-development/SKILL.md](skills/test-driven-development/SKILL.md) / [skills/test-driven-development/SKILL_CN.md](skills/test-driven-development/SKILL_CN.md)
- **dry-refactoring**（OPTIONAL）：以 DRY 为目标的系统重构流程（识别重复→抽象→替换→验证）。
  - 入口：[skills/dry-refactoring/SKILL.md](skills/dry-refactoring/SKILL.md)
- **review-code**（RECOMMENDED）：6 维度结构化审查（正确性/安全/性能/可读性/测试/架构）并产出报告。
  - 入口：[skills/review-code/SKILL.md](skills/review-code/SKILL.md)
- **review-code_pro**（RECOMMENDED）：同上，但强制叠加项目规范过滤（[skills/review-code_pro/code_spec/dreame_code.md](skills/review-code_pro/code_spec/dreame_code.md)），并要求标注建议来源。
  - 入口：[skills/review-code_pro/SKILL.md](skills/review-code_pro/SKILL.md)
- **code-review-skill**（OPTIONAL）：更偏“审查方法论+沟通话术+语言/框架清单”的 reviewer playbook。
  - 入口：[skills/code-review-skill/SKILL.md](skills/code-review-skill/SKILL.md) / [skills/code-review-skill/SKILL_CN.md](skills/code-review-skill/SKILL_CN.md)
- **pr-review-toolkit**（OPTIONAL）：PR 审查工具箱（多个专用 agent：注释/测试/静默失败/类型/简化等），适合定向扫雷。
  - 入口：[skills/pr-review-toolkit/README.md](skills/pr-review-toolkit/README.md)

### 5) 文档、发布与变更（对外表达）

- **gen_readme**（RECOMMENDED）：为 C 项目或单个 .c 文件生成结构化 README。
  - 入口：[skills/gen_readme/SKILL.md](skills/gen_readme/SKILL.md)
- **changelog-generator**（RECOMMENDED）：从 git 历史生成面向用户的变更日志/发布说明。
  - 入口：[skills/changelog-generator/SKILL.md](skills/changelog-generator/SKILL.md) / [skills/changelog-generator/SKILL_CN.md](skills/changelog-generator/SKILL_CN.md)
- **git-commit-viewer**（MUST，按场景）：当用户要“看某个 commit 的具体 diff”时，用它产出可分享的 Markdown 结果。
  - 入口：[skills/git-commit-viewer/SKILL.md](skills/git-commit-viewer/SKILL.md) / [skills/git-commit-viewer/SKILL_CN.md](skills/git-commit-viewer/SKILL_CN.md)

### 6) 检索与素材抽取（信息输入）

- **local-knowledge-retrieval**（MUST，按场景）：当用户要查本仓库 KnowledgeBase/ 的内容时，必须走它的 KB 规则（先读 KB README 再检索）。
  - 入口：[skills/local-knowledge-retrieval/SKILL.md](skills/local-knowledge-retrieval/SKILL.md)
- **article-extractor**（RECOMMENDED）：从外部 URL 抽取干净的正文（去广告/导航）。
  - 入口：[skills/article-extractor/SKILL.md](skills/article-extractor/SKILL.md) / [skills/article-extractor/SKILL_CN.md](skills/article-extractor/SKILL_CN.md)

---

## 选型对比（同类技能怎么选）

### A) “我要改代码/做实现”

- **explorer**：只定位/读，不改文件；适合快速摸清入口与调用链。
- **coder**：直接落地改代码并验证；适合明确目标后的执行。
- **architect / plan**：先把路线、风险、验收对齐；适合复杂/多方案任务。
- **coding-agent**：把大任务委托给外部编码代理（后台跑、会话监控）；适合重构/大功能/批处理。

### B) “我要做代码审查/质量把关”

- **review-code**：一条龙 6 维度审查 + 结构化报告；适合需要可追溯结论。
- **review-code_pro**：在 review-code 基础上强制项目规范（[skills/review-code_pro/code_spec/dreame_code.md](skills/review-code_pro/code_spec/dreame_code.md)）过滤与来源标注；适合“项目规约高于通用规范”的团队。
- **code-review-skill**：审查心态/沟通与语言清单；适合培养 reviewer 能力、统一评审话术。
- **pr-review-toolkit**：拆分成多个专用 agent 的工具箱；适合 PR 需要定向扫雷（测试缺口/静默失败/类型设计等）。

### C) “我要产出文档/对外说明”

- **gen_readme**：面向“当前代码结构”的 README（尤其 C 项目）。
- **changelog-generator**：面向“变化历史”的发布说明/变更日志（多 commit 汇总）。
- **git-commit-viewer**：面向“单次提交”的精确 diff 产物（可分享 Markdown）。
- **article-extractor**：面向“外部网页文章”的正文抽取（提供干净输入材料）。

### D) “我要隔离环境/并行开发”

- **using-git-worktrees**：把隔离变成流程（目录选择→ignore 校验→基线测试）；适合并行分支、多任务同时跑，且不污染主工作区。


