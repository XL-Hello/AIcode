# Code Range Extraction Template

> 用途：用于子代理输出“代码区间提取”阶段的标准结果。
> 适用范围：仅覆盖提交提取与变更摘要，不包含代码评审结论。
> **限制条件**：仅输出扩展名为 `.c`, `.h`, `.inc` 的文件代码修改内容，其他文件（如 `.md`, `.json`, `.txt`, `.data`, `.bin`, `.sh`, `Makefile` 等）必须过滤。
> 使用方式：将 {{占位符}} 替换为真实内容；提交块可按需重复。

## 项目: {{module}} | 分支: {{branch}}

### 提交概览
- 时间范围: {{start_date}} ~ {{end_date}}
- 提交总数: {{commit_count}}
- 涉及作者: {{authors}}

### 详细提交记录
<!-- 可按需重复以下行 -->
- `{{commit_sha}}` | {{author}} | {{commit_time}} | {{commit_message}}
- `{{commit_sha}}` | {{author}} | {{commit_time}} | {{commit_message}}

### 详细提交记录展开

#### Commit: {{commit_hash}} | Author: {{author}} | Date: {{commit_time}}
**提交信息**: {{commit_message}}

**变更摘要**:
<!-- 可按需重复以下行；需覆盖该 commit 影响的所有文件 -->
- {{file_path}} | {{action}} | +{{added_lines}} / -{{deleted_lines}}
- {{file_path}} | {{action}} | +{{added_lines}} / -{{deleted_lines}}

**关键代码变更**:
<!-- 可按需重复以下块；需罗列该 commit 的所有代码修改片段（去上下文） -->
- {{file_path}}:{{start_line}}-{{end_line}} | {{action}}
	{{code_change_fragment}}
- {{file_path}}:{{start_line}}-{{end_line}} | {{action}}
	{{code_change_fragment}}

---

*Generated at: {{generated_time}}*