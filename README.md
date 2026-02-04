# AIcode
一个嵌入式AICode的skills工程。

使用方法：
- 将目标项目放在 [projects](projects) 下。
- 然后利用 [skills](skills) 下的方法进行相关的AI操作。

目录：
- [projects](projects)
- [skills](skills)

## Skills 概述

以下是 [skills](skills) 文件夹下的所有技能及其简短描述：

- **article-extractor**: 从URL提取干净的文章内容（博客文章、教程等），去除广告和导航，保存为可读文本。
- **changelog-generator**: 从git提交自动生成面向用户的变更日志，将技术提交转换为清晰的客户友好发布说明。
- **file-organizer**: 智能组织计算机上的文件和文件夹，查找重复项，建议更好的结构，并自动化清理任务。
- **prompt-engineering**: 用于编写命令、钩子、技能或提示，包括优化提示、改进LLM输出或设计生产提示模板。
- **review-code**: 全面的代码审查技能，涵盖正确性、安全性、性能、可读性、测试和架构六个维度。
- **ship-learn-next**: 将学习内容（如YouTube转录、文章、教程）转换为可操作的实施计划，使用Ship-Learn-Next框架。
- **software-architecture**: 质量导向的软件架构指南，基于Clean Architecture和Domain Driven Design原则。
- **test-driven-development**: 测试驱动开发技能，在编写实现代码前先写测试。
- **using-git-worktrees**: 创建隔离的git工作树，用于功能开发或实施计划执行，具有智能目录选择和安全验证。

## Skills: review-code

### 触发方式
在对话中使用以下触发词即可启动：review code / code review / 审查代码 / 代码审查。

### AI内执行流程
1. 收集上下文：询问审查路径，识别语言/框架/规模并记录。
2. 快速扫描：定位高风险区域与明显问题。
3. 深入审查（6个维度）：正确性 → 安全性 → 性能 → 可读性 → 测试 → 架构。
4. 生成报告：汇总问题并输出结构化报告。
5. 完成审查：保存最终状态与摘要。

### 强制前置阅读
在执行任何审查前，必须阅读以下规范：
- [skills/review-code/specs/review-dimensions.md](skills/review-code/specs/review-dimensions.md)
- [skills/review-code/specs/issue-classification.md](skills/review-code/specs/issue-classification.md)
- [skills/review-code/specs/quality-standards.md](skills/review-code/specs/quality-standards.md)

### 产出（自动生成）
- 工作目录：.workflow/.scratchpad/review-code-YYYYMMDDHHMMSS（位于 [.workflow/.scratchpad](.workflow/.scratchpad)）
- 审查状态与上下文：
  - [.workflow/.scratchpad/state.json](.workflow/.scratchpad/state.json)
  - [.workflow/.scratchpad/context.json](.workflow/.scratchpad/context.json)
- 维度问题清单：
  - [.workflow/.scratchpad/findings](.workflow/.scratchpad/findings)
- 最终审查报告：
  - [.workflow/.scratchpad/review-report.md](.workflow/.scratchpad/review-report.md)

### 参考
- [skills/review-code/SKILL.md](skills/review-code/SKILL.md)
- [skills/review-code/phases/orchestrator.md](skills/review-code/phases/orchestrator.md)

## Skills: article-extractor

### 触发方式
当用户提供文章或博客的URL，并希望提取文本内容时激活，例如："下载这篇文章"、"从[URL]提取内容"、"保存这个博客文章为文本"。

### AI内执行流程
1. 检查工具安装（reader或trafilatura）。
2. 使用最佳可用工具下载并提取文章。
3. 清理内容（去除多余空白，正确格式化）。
4. 以文章标题为文件名保存到文件。
5. 确认保存位置并显示内容预览。

### 产出（自动生成）
- 提取的文章文本文件，保存在工作目录中。

### 参考
- [skills/article-extractor/SKILL.md](skills/article-extractor/SKILL.md)

## Skills: changelog-generator

### 触发方式
当需要准备发布说明、创建产品更新摘要或生成变更日志时激活，例如："从上次发布以来创建变更日志"、"为版本2.5.0生成发布说明"。

### AI内执行流程
1. 扫描Git历史：分析指定时间段或版本间的提交。
2. 分类变更：将提交分组为功能、改进、错误修复、破坏性变更、安全性等类别。
3. 转换为用户友好语言：将技术提交转换为客户语言。
4. 专业格式化：创建清洁、结构化的变更日志条目。
5. 过滤噪音：排除内部提交（重构、测试等）。
6. 遵循最佳实践：应用变更日志指南和品牌声音。

### 产出（自动生成）
- 结构化的变更日志文件，通常为Markdown格式。

### 参考
- [skills/changelog-generator/SKILL.md](skills/changelog-generator/SKILL.md)

## Skills: file-organizer

### 触发方式
当文件和文件夹混乱、需要查找重复文件、建立更好组织习惯或清理项目时激活，例如："组织我的下载文件夹"、"查找文档文件夹中的重复文件"。

### AI内执行流程
1. 分析当前结构：审查文件夹和文件以了解内容。
2. 查找重复项：识别系统中的重复文件。
3. 建议组织：基于内容提出逻辑文件夹结构。
4. 自动化清理：经批准后移动、重命名和组织文件。
5. 保持上下文：基于文件类型、日期和内容做出智能决策。
6. 减少杂乱：识别可能不再需要的旧文件。

### 产出（自动生成）
- 重新组织的文件结构和清理报告。

### 参考
- [skills/file-organizer/SKILL.md](skills/file-organizer/SKILL.md)

## Skills: prompt-engineering

### 触发方式
当编写命令、钩子、技能、提示或优化LLM交互时激活，包括改进提示、优化输出或设计生产提示模板。

### AI内执行流程
1. 应用Few-Shot Learning：通过示例教导模型行为。
2. 使用Chain-of-Thought Prompting：请求逐步推理。
3. 优化提示：迭代改进提示以获得更好结果。
4. 设计模板：创建可重用的生产级提示模板。
5. 测试和验证：确保提示在不同场景下工作。

### 产出（自动生成）
- 优化后的提示模板和示例输出。

### 参考
- [skills/prompt-engineering/SKILL.md](skills/prompt-engineering/SKILL.md)

## Skills: ship-learn-next

### 触发方式
当用户有转录、文章或教程，并希望将其转换为可操作计划时激活，例如："实施这个建议"、"将这个变成计划"、"从教育内容中提取实施步骤"。

### AI内执行流程
1. 阅读内容：分析用户提供的文件（转录、文章、笔记）。
2. 提取核心教训：识别主要建议、可操作原则、技能和示例。
3. 创建Ship-Learn-Next周期：为每个教训设计可发货的迭代。
4. 生成实施计划：将学习转换为具体行动步骤。
5. 制定学习任务：创建可重复的练习和改进循环。

### 产出（自动生成）
- 结构化的实施计划文件，包含Ship-Learn-Next周期。

### 参考
- [skills/ship-learn-next/SKILL.md](skills/ship-learn-next/SKILL.md)

## Skills: software-architecture

### 触发方式
当用户想要编写代码、设计架构、分析代码或进行任何软件开发相关活动时激活。

### AI内执行流程
1. 应用Clean Architecture和DDD原则：分离领域实体和基础设施关注点。
2. 遵循代码风格规则：使用早期返回、避免重复、分解长函数。
3. 采用库优先方法：搜索现有解决方案而非自定义代码。
4. 实施最佳实践：使用领域特定命名、保持关注点分离。
5. 设计架构：定义用例并保持隔离。

### 产出（自动生成）
- 符合质量标准的代码结构和架构文档。

### 参考
- [skills/software-architecture/SKILL.md](skills/software-architecture/SKILL.md)

## Skills: test-driven-development

### 触发方式
在实现任何功能或修复错误前激活，始终在编写实现代码前写测试。

### AI内执行流程
1. 编写测试：先写失败的测试。
2. 观看失败：确保测试确实测试正确的东西。
3. 编写最小代码：仅编写通过测试所需的最少代码。
4. 重构：改进代码而不改变行为。
5. 重复：红-绿-重构循环。

### 产出（自动生成）
- 测试套件和通过测试的实现代码。

### 参考
- [skills/test-driven-development/SKILL.md](skills/test-driven-development/SKILL.md)

## Skills: using-git-worktrees

### 触发方式
当开始需要与当前工作区隔离的功能工作或执行实施计划前激活。

### AI内执行流程
1. 选择目录：按照优先级检查现有目录或询问用户。
2. 创建工作树：使用git worktree命令创建隔离工作区。
3. 安全验证：确保创建成功且隔离。
4. 设置工作区：导航到新工作树并准备开发。
5. 宣布开始：通知用户正在使用此技能。

### 产出（自动生成）
- 隔离的git工作树目录，用于独立开发。

### 参考
- [skills/using-git-worktrees/SKILL.md](skills/using-git-worktrees/SKILL.md)

