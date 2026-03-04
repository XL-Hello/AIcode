# Code Review Report Template

> 用途：用于生成任意项目的代码审查输出。
> 使用方式：将 `{{占位符}}` 替换为真实内容；不适用的模块可删除。

## 审查概览

| 项目 | 值 |
|------|------|
| 项目名称 | {{project_name}} |
| 目标路径 | {{target_path}} |
| 分支 | {{branch_name}} |
| 时间范围 | {{start_time}} ~ {{end_time}} |
| 提交总数 | {{commit_count}} |
| 涉及作者 | {{authors}} |
| 审查人 | {{reviewer}} |
| 审查时间 | {{review_date}} |

## 问题统计

| 严重程度 | 数量 |
|----------|------|
| 🔴 Critical | {{critical_count}} |
| 🟠 High | {{high_count}} |
| 🟡 Medium | {{medium_count}} |
| 🔵 Low | {{low_count}} |
| ⚪ Info | {{info_count}} |
| **总计** | **{{total_count}}** |

### 按维度统计

| 维度 | 问题数 |
|------|--------|
| Correctness (正确性) | {{correctness_count}} |
| Security (安全性) | {{security_count}} |
| Performance (性能) | {{performance_count}} |
| Readability (可读性) | {{readability_count}} |
| Testing (测试) | {{testing_count}} |
| Architecture (架构) | {{architecture_count}} |

---

## 高风险区域

| 文件/模块 | 原因 | 优先级 |
|------|------|--------|
| `{{file_or_module_1}}` | {{risk_reason_1}} | {{priority_1}} |
| `{{file_or_module_2}}` | {{risk_reason_2}} | {{priority_2}} |

---

## 代码评审意见

<!-- 每个问题按以下结构新增一节 -->

### {{severity_emoji}} [{{issue_id}}] {{issue_tag}}
- **严重程度**: {{severity}}
- **文件**: `{{file_path}}`:{{line_or_range}}
- **描述**: {{issue_description}}
- **影响**: {{issue_impact}}
- **建议**: {{fix_suggestion}}
- **建议来源**: {{rule_source}}

---

## 审查结论

### 必须修复 (Must Fix)
- {{must_fix_item_1}}
- {{must_fix_item_2}}

### 建议改进 (Should Fix)
- {{should_fix_item_1}}
- {{should_fix_item_2}}

### 可选优化 (Nice to Have)
- {{nice_to_have_item_1}}
- {{nice_to_have_item_2}}

## 通过条件（可选）
- [ ] 所有 Critical/High 问题已关闭
- [ ] 必须修复项已验证
- [ ] 关键路径回归已完成
- [ ] 风险已同步给相关负责人

---

*报告生成时间: {{generated_time}}*
