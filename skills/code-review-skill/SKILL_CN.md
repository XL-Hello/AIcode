---
name: code-review-excellence
description: |
  提供 React 19、Vue 3、Rust、TypeScript、Java、Python 和 C/C++ 的全面代码审查指导。
  帮助发现bug、改进代码质量，并提供建设性反馈。
  使用时机：审查拉取请求、进行PR审查、代码审查、审查代码变更、
  建立审查标准、指导开发人员、架构审查、安全审计、
  检查代码质量、发现bug、对代码提供反馈。
allowed-tools:
  - Read
  - Grep
  - Glob
  - Bash      # 运行 lint/test/build 命令验证代码质量
  - WebFetch  # 查阅最新文档和最佳实践
---

# 代码审查卓越

通过建设性反馈、系统分析和协作改进，将代码审查从把关转变为知识共享。

## 何时使用这个技能

- 审查拉取请求和代码变更
- 为团队建立代码审查标准
- 通过审查指导初级开发人员
- 进行架构审查
- 创建审查清单和指南
- 改进团队协作
- 减少代码审查周期时间
- 维护代码质量标准

## 核心原则

### 1. 审查心态

**代码审查的目标：**
- 发现bug和边缘情况
- 确保代码可维护性
- 在团队中分享知识
- 执行编码标准
- 改进设计和架构
- 建立团队文化

**不是目标：**
- 炫耀知识
- 吹毛求疵格式（使用linter）
- 不必要地阻止进度
- 重写为你的偏好

### 2. 有效反馈

**好的反馈是：**
- 具体且可操作
- 教育性，不是判断性
- 专注于代码，不是人
- 平衡（也赞美好的工作）
- 优先级（关键 vs 锦上添花）

```markdown
❌ 坏： "这是错的。"
✅ 好： "这可能在多个用户同时访问时导致竞态条件。考虑在这里使用互斥锁。"

❌ 坏： "为什么你不使用X模式？"
✅ 好： "你考虑过Repository模式吗？它会使这个更容易测试。这里是一个例子：[链接]"

❌ 坏： "重命名这个变量。"
✅ 好： "[nit] 考虑使用 `userCount` 而不是 `uc` 以提高清晰度。如果你喜欢保留它，不是阻塞。"
```

### 3. 审查范围

**要审查的内容：**
- 逻辑正确性和边缘情况
- 安全漏洞
- 性能影响
- 测试覆盖率和质量
- 错误处理
- 文档和注释
- API设计和命名
- 架构契合

**手动不审查的内容：**
- 代码格式（使用Prettier、Black等）
- 导入组织
- Linting违规
- 简单拼写错误

## 审查过程

### 阶段1：上下文收集（2-3分钟）

在深入代码之前，理解：
1. 阅读PR描述和链接的问题
2. 检查PR大小（>400行？要求拆分）
3. 审查CI/CD状态（测试通过？）
4. 理解业务需求
5. 注意任何相关架构决策

### 阶段2：高层审查（5-10分钟）

1. **架构与设计** - 解决方案是否适合问题？
   - 对于重大变更，咨询 [架构审查指南](reference/architecture-review-guide.md)
   - 检查：SOLID原则、耦合/内聚、反模式
2. **性能评估** - 有性能问题吗？
   - 对于性能关键代码，咨询 [性能审查指南](reference/performance-review-guide.md)
   - 检查：算法复杂度、N+1查询、内存使用
3. **文件组织** - 新文件是否在正确位置？
4. **测试策略** - 有测试覆盖边缘情况吗？

### 阶段3：逐行审查（10-20分钟）

对于每个文件，检查：
- **逻辑与正确性** - 边缘情况、off-by-one、空检查、竞态条件
- **安全** - 输入验证、注入风险、XSS、敏感数据
- **性能** - N+1查询、不必要的循环、内存泄漏
- **可维护性** - 清晰名称、单一责任、注释

### 阶段4：总结与决策（2-3分钟）

1. 总结关键问题
2. 突出你喜欢的内容
3. 做出明确决策：
   - ✅ 批准
   - 💬 评论（小建议）
   - 🔄 请求变更（必须解决）
4. 如果复杂，提供配对

## 审查技巧

### 技巧1：清单方法

使用清单进行一致审查。见 [安全审查指南](reference/security-review-guide.md) 获取全面安全清单。

### 技巧2：问题方法

而不是陈述问题，问问题：

```markdown
❌ "如果列表为空，这会失败。"
✅ "如果 `items` 是空数组，会发生什么？"

❌ "你需要在这里处理错误。"
✅ "如果API调用失败，这应该如何表现？"
```

### 技巧3：建议，不要命令

使用协作语言：

```markdown
❌ "你必须改变这个使用async/await"
✅ "建议：async/await可能使这个更可读。你怎么想？"

❌ "提取这个到一个函数"
✅ "这个逻辑出现在3个地方。提取它有意义吗？"
```

### 技巧4：区分严重性

使用标签指示优先级：

- 🔴 `[blocking]` - 合并前必须修复
- 🟡 `[important]` - 应该修复，如果不同意讨论
- 🟢 `[nit]` - 锦上添花，不是阻塞
- 💡 `[suggestion]` - 考虑的替代方法
- 📚 `[learning]` - 教育性评论，无需行动
- 🎉 `[praise]` - 好工作，继续！

## 语言特定指南

根据审查的代码语言，查阅对应的详细指南：

| 语言/框架 | 参考文件 | 关键主题 |
|-------------------|----------------|------------|
| **React** | [React指南](reference/react.md) | Hooks, useEffect, React 19 Actions, RSC, Suspense, TanStack Query v5 |
| **Vue 3** | [Vue指南](reference/vue.md) | Composition API, 响应性系统, Props/Emits, Watchers, Composables |
| **Rust** | [Rust指南](reference/rust.md) | 所有权/借用, Unsafe审查, 异步代码, 错误处理 |
| **TypeScript** | [TypeScript指南](reference/typescript.md) | 类型安全, async/await, 不可变性 |
| **Python** | [Python指南](reference/python.md) | 可变默认参数, 异常处理, 类属性 |
| **Java** | [Java指南](reference/java.md) | Java 17/21新特性, Spring Boot 3, 虚拟线程, Stream/Optional |
| **Go** | [Go指南](reference/go.md) | 错误处理, goroutine/channel, context, 接口设计 |
| **C** | [C指南](reference/c.md) | 指针/缓冲区, 内存安全, UB, 错误处理 |
| **C++** | [C++指南](reference/cpp.md) | RAII, 生命周期, Rule of 0/3/5, 异常安全 |
| **CSS/Less/Sass** | [CSS指南](reference/css-less-sass.md) | 变量规范, !important, 性能优化, 响应式, 兼容性 |
| **Qt** | [Qt指南](reference/qt.md) | 对象模型, 信号/槽, 内存管理, 线程安全, 性能 |

## 额外资源

- [架构审查指南](reference/architecture-review-guide.md) - 架构设计审查指南（SOLID、反模式、耦合度）
- [性能审查指南](reference/performance-review-guide.md) - 性能审查指南（Web Vitals、N+1、复杂度）
- [常见错误清单](reference/common-bugs-checklist.md) - 按语言分类的常见错误清单
- [安全审查指南](reference/security-review-guide.md) - 安全审查指南
- [代码审查最佳实践](reference/code-review-best-practices.md) - 代码审查最佳实践
- [PR审查模板](assets/pr-review-template.md) - PR审查评论模板
- [审查清单](assets/review-checklist.md) - 快速参考清单