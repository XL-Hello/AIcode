---
name: using-superpowers
description: 当开始任何对话时使用 - 建立如何查找和使用技能，要求在任何响应（包括澄清问题）之前调用技能工具
---

<EXTREMELY-IMPORTANT>
如果你认为技能甚至有1%的机会适用于你正在做的事情，你绝对必须调用技能。

如果技能适用于你的任务，你没有选择。你必须使用它。

这不是可协商的。这不是可选的。你不能合理化你的方式摆脱这个。
</EXTREMELY-IMPORTANT>

## 如何访问技能

**在Claude Code中：** 使用 `Skill` 工具。当你调用技能时，其内容被加载并呈现给你——直接跟随它。永远不要在技能文件上使用Read工具。

**在其他环境中：** 检查你的平台的文档以了解技能如何加载。

# 使用技能

## 规则

**在任何响应或行动之前调用相关或请求的技能。** 即使技能有1%的机会适用于情况，你也应该调用技能来检查。如果调用的技能对情况不合适，你不需要使用它。

```dot
digraph skill_flow {
    "User message received" [shape=doublecircle];
    "About to EnterPlanMode?" [shape=doublecircle];
    "Already brainstormed?" [shape=diamond];
    "Invoke brainstorming skill" [shape=box];
    "Might any skill apply?" [shape=diamond];
    "Invoke Skill tool" [shape=box];
    "Announce: 'Using [skill] to [purpose]'" [shape=box];
    "Has checklist?" [shape=diamond];
    "Create TodoWrite todo per item" [shape=box];
    "Follow skill exactly" [shape=box];
    "Respond (including clarifications)" [shape=doublecircle];

    "About to EnterPlanMode?" -> "Already brainstormed?";
    "Already brainstormed?" -> "Invoke brainstorming skill" [label="no"];
    "Already brainstormed?" -> "Might any skill apply?" [label="yes"];
    "Invoke brainstorming skill" -> "Might any skill apply?";

    "User message received" -> "Might any skill apply?";
    "Might any skill apply?" -> "Invoke Skill tool" [label="yes, even 1%"];
    "Might any skill apply?" -> "Respond (including clarifications)" [label="definitely not"];
    "Invoke Skill tool" -> "Announce: 'Using [skill] to [purpose]'";
    "Announce: 'Using [skill] to [purpose]'" -> "Has checklist?";
    "Has checklist?" -> "Create TodoWrite todo per item" [label="yes"];
    "Has checklist?" -> "Follow skill exactly" [label="no"];
    "Create TodoWrite todo per item" -> "Follow skill exactly";
}
```

## 红旗

这些想法意味着停止——你在合理化：

| 想法 | 现实 |
|---------|---------|
| "这只是一个简单问题" | 问题是任务。检查技能。 |
| "我需要先更多上下文" | 技能检查在澄清问题之前。 |
| "让我先探索代码库" | 技能告诉你如何探索。先检查。 |
| "我可以快速检查git/文件" | 文件缺乏对话上下文。检查技能。 |
| "让我先收集信息" | 技能告诉你如何收集信息。 |
| "这不需要正式技能" | 如果技能存在，使用它。 |
| "我记得这个技能" | 技能会演变。阅读当前版本。 |
| "这不算作任务" | 行动 = 任务。检查技能。 |
| "技能过度" | 简单事情变得复杂。使用它。 |
| "我先做这件事" | 在做任何事情之前检查。 |
| "这感觉有成效" | 无纪律行动浪费时间。技能防止这个。 |
| "我知道那意味着什么" | 知道概念 ≠ 使用技能。调用它。 |

## 技能优先级

当多个技能可能适用时，使用这个顺序：

1. **过程技能优先** (brainstorming, debugging) - 这些确定如何接近任务
2. **实施技能其次** (frontend-design, mcp-builder) - 这些指导执行

"让我们构建X" → 先brainstorming，然后实施技能。
"修复这个bug" → 先debugging，然后领域特定技能。

## 技能类型

**刚性** (TDD, debugging): 完全跟随。不要适应远离纪律。

**灵活** (patterns): 将原则适应上下文。

技能本身告诉你哪个。

## 用户指令

指令说WHAT，不是HOW。"添加X"或"修复Y"并不意味着跳过工作流。