---
name: shell-scripting
description: Shell 脚本最佳实践和模式。当编写 bash/zsh 脚本、自动化任务、创建 CLI 工具或调试 shell 命令时使用。
author: Joseph OBrien
status: unpublished
updated: '2025-12-23'
version: 1.0.1
tag: skill
type: skill
---

# Shell 脚本

涵盖 bash/zsh 模式、自动化、错误处理和 CLI 工具开发的全面 shell 脚本技能。

## 何时使用此技能

- 编写自动化脚本
- 创建 CLI 工具
- 系统管理任务
- 构建和部署脚本
- 日志处理和分析
- 文件操作和批量操作
- Cron 作业和计划任务

## 脚本结构

### 模板

```bash
#!/usr/bin/env bash
# Script: name.sh
# Description: What this script does
# Usage: ./name.sh [options] <args>

set -euo pipefail  # Exit on error, undefined vars, pipe failures
IFS=$'\n\t'        # Safer word splitting

# Constants
readonly SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
readonly SCRIPT_NAME="$(basename "${BASH_SOURCE[0]}")"

# Default values
VERBOSE=false
DRY_RUN=false

# Functions
usage() {
    cat <<EOF
Usage: $SCRIPT_NAME [options] <argument>

Options:
    -h, --help      Show this help message
    -v, --verbose   Enable verbose output
    -n, --dry-run   Show what would be done
EOF
}

log() {
    echo "[$(date +'%Y-%m-%d %H:%M:%S')] $*" >&2
}

error() {
    log "ERROR: $*"
    exit 1
}

# Main logic
main() {
    # Parse arguments
    while [[ $# -gt 0 ]]; do
        case "$1" in
            -h|--help)
                usage
                exit 0
                ;;
            -v|--verbose)
                VERBOSE=true
                shift
                ;;
            -n|--dry-run)
                DRY_RUN=true
                shift
                ;;
            *)
                break
                ;;
        esac
    done

    # Your logic here
}

main "$@"
```

## 错误处理

### 设置选项

```bash
set -e          # 任何错误时退出
set -u          # 未定义变量时错误
set -o pipefail # 管道失败是脚本失败
set -x          # 调试：打印每个命令（谨慎使用）
```

### 清理陷阱

```bash
cleanup() {
    rm -f "$TEMP_FILE"
    log "Cleanup complete"
}
trap cleanup EXIT

# 也处理特定信号
trap 'error "Script interrupted"' INT TERM
```

### 错误检查模式

```bash
# 检查命令存在
command -v jq >/dev/null 2>&1 || error "jq is required but not installed"

# 检查文件存在
[[ -f "$FILE" ]] || error "File not found: $FILE"

# 检查目录存在
[[ -d "$DIR" ]] || mkdir -p "$DIR"

# 检查变量已设置
[[ -n "${VAR:-}" ]] || error "VAR is not set"

# 明确检查退出状态
if ! some_command; then
    error "some_command failed"
fi
```

## 变量和替换

### 变量扩展

```bash
# 默认值
${VAR:-default}     # 如果 VAR 未设置或为空，使用默认值
${VAR:=default}     # 如果未设置，将 VAR 设置为默认值
${VAR:+value}       # 如果 VAR 已设置，使用值
${VAR:?error msg}   # 如果 VAR 未设置或为空，错误

# 字符串操作
${VAR#pattern}      # 移除最短前缀匹配
${VAR##pattern}     # 移除最长前缀匹配
${VAR%pattern}      # 移除最短后缀匹配
${VAR%%pattern}     # 移除最长后缀匹配
${VAR/old/new}      # 替换第一次出现
${VAR//old/new}     # 替换所有出现
${#VAR}             # VAR 的长度
```

### 数组

```bash
# 声明数组
declare -a ARRAY=("one" "two" "three")

# 访问元素
echo "${ARRAY[0]}"     # 第一个元素
echo "${ARRAY[@]}"     # 所有元素
echo "${#ARRAY[@]}"    # 元素数量
echo "${!ARRAY[@]}"    # 所有索引

# 迭代
for item in "${ARRAY[@]}"; do
    echo "$item"
done

# 追加
ARRAY+=("four")
```

### 关联数组

```bash
declare -A MAP
MAP["key1"]="value1"
MAP["key2"]="value2"

# 访问
echo "${MAP[key1]}"

# 检查键存在
[[ -v MAP[key1] ]] && echo "key1 exists"

# 迭代
for key in "${!MAP[@]}"; do
    echo "$key: ${MAP[$key]}"
done
```

## 控制流

### 条件

```bash
# 字符串比较
[[ "$str" == "value" ]]
[[ "$str" != "value" ]]
[[ -z "$str" ]]  # 空
[[ -n "$str" ]]  # 非空

# 数值比较
[[ "$num" -eq 5 ]]  # 等于
[[ "$num" -ne 5 ]]  # 不等于
[[ "$num" -lt 5 ]]  # 小于
[[ "$num" -gt 5 ]]  # 大于

# 文件测试
[[ -f "$file" ]]  # 文件存在
[[ -d "$dir" ]]   # 目录存在
[[ -r "$file" ]]  # 可读
[[ -w "$file" ]]  # 可写
[[ -x "$file" ]]  # 可执行

# 逻辑运算符
[[ "$a" && "$b" ]]  # AND
[[ "$a" || "$b" ]]  # OR
[[ ! "$a" ]]        # NOT
```

### 循环

```bash
# For 循环
for i in {1..10}; do
    echo "$i"
done

# While 循环
while read -r line; do
    echo "$line"
done < "$file"

# 进程替换
while read -r line; do
    echo "$line"
done < <(command)

# C 风格 for
for ((i=0; i<10; i++)); do
    echo "$i"
done
```

## 输入/输出

### 读取输入

```bash
# 从用户读取
read -r -p "Enter name: " name

# 读取密码（隐藏）
read -r -s -p "Password: " password

# 带超时读取
read -r -t 5 -p "Quick! " answer

# 逐行读取文件
while IFS= read -r line; do
    echo "$line"
done < "$file"
```

### 输出和重定向

```bash
# 重定向 stdout
command > file      # 覆盖
command >> file     # 追加

# 重定向 stderr
command 2> file

# 重定向两者
command &> file
command > file 2>&1

# 丢弃输出
command > /dev/null 2>&1

# Tee（输出并保存）
command | tee file
```

## 文本处理

### 常见模式

```bash
# 查找并处理文件
find . -name "*.log" -exec grep "ERROR" {} +

# 处理 CSV
while IFS=, read -r col1 col2 col3; do
    echo "$col1: $col2"
done < file.csv

# JSON 处理（使用 jq）
jq '.key' file.json
jq -r '.items[]' file.json

# AWK 单行命令
awk '{print $1}' file           # 第一列
awk -F: '{print $1}' /etc/passwd  # 自定义分隔符
awk 'NR > 1' file               # 跳过标题

# SED 单行命令
sed 's/old/new/g' file          # 替换所有
sed -i 's/old/new/g' file       # 原地编辑
sed -n '10,20p' file            # 打印第 10-20 行
```

## 最佳实践

### 做

- 引用所有变量扩展：`"$VAR"`
- 使用 `[[ ]]` 而非 `[ ]` 进行测试
- 使用 `$(command)` 而非反引号
- 检查返回值
- 对常量使用 `readonly`
- 在函数中使用 `local`
- 提供 `--help` 选项
- 使用有意义的退出代码

### 不要

- 解析 `ls` 输出
- 对不受信任输入使用 `eval`
- 假设路径不含空格
- 忽略 shellcheck 警告
- 编写一个巨大的脚本（模块化）

## 参考文件

- **`references/one_liners.md`** - 有用的单行命令

## 与其他技能集成

- **developer-experience** - 用于工具自动化
- **debugging** - 用于脚本调试
- **testing** - 用于脚本测试模式