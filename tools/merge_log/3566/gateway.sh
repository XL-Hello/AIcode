#!/bin/bash
# 从指定日志文件中按过滤规则提取日志，输出到 <文件名>_gateway.log

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"

if [ -z "$1" ]; then
    echo "用法: $0 <源日志文件>"
    exit 1
fi

if [ ! -f "$1" ]; then
    echo "错误: 文件不存在 - $1"
    exit 1
fi

# ==================== 过滤规则配置 ====================
# 【过滤显示】只保留匹配以下任一正则的行（每行一条正则，留空则不过滤）
INCLUDE_PATTERNS=(
    '\[gateway'
    # '要额外显示的关键词2'
    # '要额外显示的关键词3'
)

# 【过滤不显示】排除匹配以下任一正则的行（每行一条正则，留空则不排除）
EXCLUDE_PATTERNS=(
    'mSend heart.*done\.'
    # '要排除的关键词2'
    # '要排除的关键词3'
)
# ======================================================

# 构建 grep 参数数组
include_args=()
for pat in "${INCLUDE_PATTERNS[@]}"; do
    [ -z "$pat" ] && continue
    include_args+=(-e "$pat")
done

exclude_args=()
for pat in "${EXCLUDE_PATTERNS[@]}"; do
    [ -z "$pat" ] && continue
    exclude_args+=(-e "$pat")
done

# 输出文件名: <原文件名>_gateway.log（在 .log 后缀前插入 _gateway）
base_name=$(basename "$1" .log)
OUTPUT="$SCRIPT_DIR/${base_name}_gateway.log"

# 执行过滤: include → exclude
if [ ${#include_args[@]} -gt 0 ]; then
    grep "${include_args[@]}" "$1" | grep -v "${exclude_args[@]}" > "$OUTPUT"
else
    grep -v "${exclude_args[@]}" "$1" > "$OUTPUT"
fi

echo "提取完成: $(basename "$OUTPUT") ($(wc -l < "$OUTPUT") 行)"
