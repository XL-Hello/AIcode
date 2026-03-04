
# 多项目代码审查系统 (Multi-Project Code Review System)

---

## 🛠 配置区块 (Configuration Section)
> **使用说明**：开始执行前请根据实际环境修改以下 YAML 变量。

```yaml
config:
   # 工作区根路径（执行命令获取当前路径）
   base_path: "$(pwd)"

   # 主工程路径（相对于 base_path）
   base_project_relative_path: "projects/dreame_rtos_4inch_project"
   base_project_path: "${base_path}/${base_project_relative_path}"

   # 子项目列表目录（相对于 base_project_path）
   subproject_table_relative_path: "WB100-SDK/apps"

   # 输出路径（相对于 base_path，{{DATE}} 在执行时替换）
   temp_output_relative_path: ".workspace/.temp_{{DATE}}/app"
   final_output_relative_path: ".workspace/.temp_{{DATE}}"
   temp_output_path: "${base_path}/${temp_output_relative_path}"
   final_output_path: "${base_path}/${final_output_relative_path}"

   # 时间配置
   review_days: 10  # 审查最近 N 天的提交

   # Git 作者配置
   authors: "all"  # 可选: "all" 或具体作者名，如 "zhangsan,lisi"

   # 子项目清单（模块名:分支名）
   subprojects:
    - { module: "WB100-SDK/apps/family", branch: "dev_rtos" }
    - { module: "WB100-SDK/apps/devicemanager", branch: "dev_rtos" }
    - { module: "dreame/flash/img/resource/dreame_model", branch: "dev-1.1.2-ALL" }
    - { module: "WB100-SDK/apps/flashdb", branch: "master" }
    - { module: "WB100-SDK/apps/bus_server", branch: "rtos_dev" }
    - { module: "WB100-SDK/apps/awtk_launch", branch: "dev-rtos" }
    - { module: "WB100-SDK/apps/dre_json", branch: "rtos_dev" }
    - { module: "WB100-SDK/apps/dre_log", branch: "rtos_dev" }
    - { module: "WB100-SDK/apps/dre_platrom", branch: "rtos_dev" }
    - { module: "WB100-SDK/apps/dreame_hal", branch: "dev-rtos-new" }
    - { module: "WB100-SDK/apps/dreame_partition_tools", branch: "dev-rtos" }
    - { module: "WB100-SDK/apps/env_var", branch: "rtos_dev" }
    - { module: "WB100-SDK/apps/bus", branch: "rtos_dev" }
    - { module: "WB100-SDK/apps/dre_voice", branch: "dev-rtos" }
    - { module: "WB100-SDK/apps/dre_log_server", branch: "rtos_dev" }
    - { module: "WB100-SDK/apps/dreame_ota", branch: "rtos_dev" }
    - { module: "WB100-SDK/apps/system_ctrl", branch: "rtos_dev" }
    - { module: "WB100-SDK/apps/audio_player", branch: "dev" }
    - { module: "WB100-SDK/apps/dreame_factory_client", branch: "master" }
    - { module: "WB100-SDK/apps/dreame_factory_server", branch: "dev-rtos" }
    - { module: "WB100-SDK/apps/dreame_otaupdate", branch: "master" }
    - { module: "WB100-SDK/apps/unisound", branch: "dev-rtos" }

   # 输出模板（相对于 base_path）
   code_range_extract_template: "${base_path}/code_range_extract_template.md"
   project_review_template: "${base_path}/project_review_template.md"
   project_review_all_template: "${base_path}/project_review_all_template.md"
```

> 路径拼接规则：
> - `base_path = $(pwd)`
> - `full_module_path = base_project_path + "/" + module`
> - 其余输出与模板路径均基于 `base_path` 派生。

---

## 🚀 执行流程 (Execution Flow)

### Phase 1: 环境初始化
1. **获取时间戳**：`DATE = YYYYMMDDHHMM` (例如：202603031527)。
2. **变量替换**：将配置中的 `{{DATE}}` 统一替换为实际时间戳。
3. **建立目录**：
   - 创建 `${temp_output_path}`，用于存放各子项目提取文档与评审文档。
   - 创建 `${final_output_path}`，用于存放最终整合报告。

---

### Phase 2: 多个子代理并行处理 (Sub-Agent Execution)
> 对 `${subprojects}` 中的每个项目启动 `sub-agent-${module_name}`。

#### 📋 任务定义
- **输入**：单个项目的 `module` 路径 + `branch` 分支名。
- **项目名规则**：`project_name_sanitized = module` 最后一段（例如：`WB100-SDK/apps/awtk_launch -> awtk_launch`）。
- **文档命名规则**：`${module_name_sanitized}__${doc_type}__${DATE}__${project_name_sanitized}.md`。
- **输出（均在 `${temp_output_path}` 下）**：
  - 代码区间提取文档：`${temp_output_path}/${module_name_sanitized}__extract__${DATE}__${project_name_sanitized}.md`
  - 代码评审文档：`${temp_output_path}/${module_name_sanitized}__review__${DATE}__${project_name_sanitized}.md`

#### ⚙️ 执行步骤
1. **代码区间提取** (基于 `using-git-worktrees` 技能)
   - **目标**：提取 `${review_days}` 天内 `${authors}` 的所有提交。
   - **过滤条件**：**必须**仅输出扩展名为 `.c`, `.h`的文件代码修改内容。自动跳过并过滤其他所有类型文件（如 `.md`, `.json`, `.txt`, `.data`, `.bin`, `.sh` , `.inc` 等）。
   - **分支**：切换到 `${branch}`。
   - **格式要求**：严格按照 `${code_range_extract_template}` 输出。
   - **输出文件**：`${temp_output_path}/${module_name_sanitized}__extract.md`。

2. **代码评审** (基于 `review-code_pro` 技能)
   - **输入来源**：必须基于步骤 1 的提取文档内容的范围进行评审。
   - **评审维度**：
     - **代码规范**：命名一致性、格式化、注释质量。
     - **逻辑正确性**：边界条件处理、错误兜底逻辑。
     - **安全性**：是否存在内存泄漏、越界访问风险。
     - **性能**：算法复杂度、资源占用优化。
     - **可维护性**：耦合度评估、代码重复率。
   - **输出文件**：`${temp_output_path}/${module_name_sanitized}__review.md`。

3. **资源**
   - 保留最终生成的提取文档与评审文档。
   - 评审文档格式必须严格按照 `${project_review_template}` 输出。

---

### Phase 3: 父代理整合 (Parent-Agent Aggregation)
> 启动 `parent-agent-aggregator` 进行全局汇总。

- **输入**：`${temp_output_path}` 下所有 `*__review__*.md`（默认仅聚合评审文档）。
- **输出**：`${final_output_path}/multi_project_review_report_${DATE}.md`，格式必须严格按照 `${project_review_all_template}` 输出。

#### 📊 整合规则
1. **分类汇总结构**：
   - **执行摘要**：项目总数、总提交数、P0/P1 问题统计。
   - **详细视图**：按模块分类（如：系统服务类、硬件抽象层、工具类）。
   - **跨项目共性问题**：识别并提取重复出现的 P0/P1 风险模式。
   - **优先级建议**：仅输出 P0/P1 修复建议（不输出 P2 及以下）。
2. **冲突检测**：检查不同项目间是否存在接口版本不匹配风险。
3. **证据回链（按需）**：若需追溯评审依据，可按同名规则回查对应 `*__extract__*.md` 文档。