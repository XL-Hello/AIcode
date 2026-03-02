---
name: "awtk-dev"
description: "AWTK项目开发规范检查和编译验证。Invoke when user is working on AWTK project code modifications, before code review, or when compiling AWTK applications."
---

# AWTK 项目开发规范

## 1. 代码规范检查

进行代码修改时，首先必须确保符合项目技能中的代码规范要求：

**参考文档**: `/home/xl/dreame/AIcode/skills/review-code_2/code_spec/dreame_code.md`

### 1.1 命名与代码风格

| 项目 | 规范 |
|------|------|
| 缩进风格 | 4个空格 |
| 大括号风格 | K&R 风格（左大括号与函数/结构体/枚举等在同一行） |
| 变量命名 | 驼峰命名法（首字母小写） |
| 函数命名 | 模块前缀_驼峰格式，如 `keybind_reportProp`、`dreUI_logI` |
| 文件命名 | 下划线命名法（全小写） |

### 1.2 注释要求

- 所有函数、结构体、枚举必须添加注释
- 注释使用中文
- 单行注释：`// 函数功能概述`
- 多行注释：`/* 功能概述、参数、返回值等 */`

### 1.3 代码复杂度

- 单个源文件建议最大行数：1024
- 单个函数建议最大行数：128
- 嵌套层级建议：3层及以下

### 1.4 内存管理

- `malloc`/`calloc`/`realloc` 必须与 `free` 配对使用
- `string_t*` 类型**不需要**手动释放，由内部引用计数管理

### 1.5 日志记录

- 统一使用 `dreUI_log*` 系列函数
- 禁止使用 `printf` 直接输出

## 2. 编译验证

代码修改后，必须按以下方式进行编译验证：

### 2.1 模拟器版本（推荐用于开发调试）
终端中运行执行工程中AwtkApplication文件夹下的dreame.sh脚本。

### 2.2 嵌入式版本（完整系统构建）

```sh
# 完整构建
cd /home/xl/dreame/AIcode/projects/awtk_launch/dreame_rtos_4inch_project && ./dreame.sh clean && ./dreame.sh build

# 仅 audio 核
cd /home/xl/dreame/AIcode/projects/awtk_launch/dreame_rtos_4inch_project && ./dreame.sh clean audio && ./dreame.sh build audio

# 清理构建
cd /home/xl/dreame/AIcode/projects/awtk_launch/dreame_rtos_4inch_project && ./dreame.sh clean
```

## 3. 项目结构

```
AwtkApplication/
├── src/
│   ├── main.c              # 入口点
│   ├── application.c       # 应用程序逻辑
│   ├── pages/              # 页面实现
│   └── dreame/             # Dreame 品牌功能
│       ├── cardPage/       # 卡片式 UI 组件
│       ├── custom_widgets/ # 自定义控件
│       ├── manager/        # 管理器（设备、网络、屏幕）
│       └── dataServer/     # 通信层
├── res/                    # 资源文件
└── dreame.sh               # 构建脚本（模拟器版本的编译脚本）
```

## 4. 开发工作流程

当处理 AWTK 项目时，按以下步骤执行：

1. **代码修改前**：确认理解上述规范要求
2. **代码修改时**：遵循命名规范、注释要求、内存管理规则
3. **代码修改后**：
   - 运行模拟器版本编译验证（推荐）
   - 如有需要，运行嵌入式版本完整构建
4. **提交前**：确保编译通过，无错误无警告

## 5. 快速编译命令

如果当前工作目录在 AwtkApplication 下，可以直接运行：

```sh
./dreame.sh
```

如果需要在其他位置编译，使用完整路径：

```sh
cd /home/xl/dreame/AIcode/projects/awtk_launch/dreame_rtos_4inch_project/WB100-SDK/apps/awtk_launch/AwtkApplication && ./dreame.sh
```