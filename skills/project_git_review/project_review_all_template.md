# Multi-Project P0-P1 Extraction Report Template

> 用途：聚合提取所有项目审查报告中的 P0/P1 问题（来源模板：`project_review_template.md`）。
> 使用方式：将 `{{占位符}}` 替换为真实值；仅保留 P0/P1，其他优先级可不展示。

## 提取配置

| 配置项 | 值 |
|------|------|
| 输入报告集合 | {{input_report_paths}} |
| 统计时间范围 | {{start_time}} ~ {{end_time}} |
| 作者范围 | {{author_scope}} |
| 评审规则来源 | {{review_rules}} |
| 提取执行人 | {{operator}} |
| 执行时间 | {{run_time}} |

### 优先级映射规则
- P0：`Critical` 或被标记为 `Must Fix（合并前阻塞）`
- P1：`High` 或被标记为 `Should Fix（本迭代必须完成）`
- 去重键建议：`{{project}} + {{issue_id}} + {{file}} + {{line_or_range}}`

## 执行摘要（仅 P0/P1）

| 指标 | 数值 |
|------|------|
| 扫描报告总数 | {{report_total}} |
| 命中项目数（含 P0/P1） | {{affected_project_count}} |
| P0 数量 | {{p0_count}} |
| P1 数量 | {{p1_count}} |
| P0+P1 总数 | {{p0_p1_total}} |

## 项目命中总览

| 项目/模块 | 分支 | P0 | P1 | 状态 | 关联报告 |
|------|------|----|----|------|------|
| {{project_name_1}} | {{branch_1}} | {{p0_1}} | {{p1_1}} | {{status_1}} | {{report_path_1}} |
| {{project_name_2}} | {{branch_2}} | {{p0_2}} | {{p1_2}} | {{status_2}} | {{report_path_2}} |

## P0 问题清单（必须阻塞）

| 编号 | 项目 | 问题ID | 标签 | 文件位置 | 问题描述 | 风险影响 | 建议动作 | 负责人 | 状态 |
|------|------|--------|------|----------|----------|----------|----------|--------|------|
| {{index}} | {{project}} | {{issue_id}} | {{issue_tag}} | `{{file_path}}:{{line_or_range}}` | {{description}} | {{impact}} | {{action}} | {{owner}} | {{status}} |

## P1 问题清单（本迭代必须完成）

| 编号 | 项目 | 问题ID | 标签 | 文件位置 | 问题描述 | 风险影响 | 建议动作 | 负责人 | 状态 |
|------|------|--------|------|----------|----------|----------|----------|--------|------|
| {{index}} | {{project}} | {{issue_id}} | {{issue_tag}} | `{{file_path}}:{{line_or_range}}` | {{description}} | {{impact}} | {{action}} | {{owner}} | {{status}} |

## 跨项目共性（仅 P0/P1）

- 共性模式 1：{{common_pattern_1}}
- 共性模式 2：{{common_pattern_2}}
- 根因归类：{{root_cause_summary}}

## 修复推进建议

### 本周必须完成
- {{must_do_1}}
- {{must_do_2}}

### 风险缓解动作
- {{mitigation_1}}
- {{mitigation_2}}

## 质量门禁结论

- 门禁规则：{{gate_rule}}
- 判定结果：**{{gate_result}}**
- 判定依据：{{gate_reason}}

## 产物与追踪

- 原始子报告目录：{{child_report_dir}}
- 聚合报告路径：{{aggregate_report_path}}
- 问题跟踪链接（Jira/禅道/GitHub Issues）：{{tracking_link}}

---

*Generated at: {{generated_time}}*