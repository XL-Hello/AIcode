#!/bin/bash
# Git Commit Viewer - Bash版本
# 根据commit号查询相关代码变更并输出到Markdown文件

set -e

# 检查参数
if [ $# -lt 2 ]; then
    echo "用法: $0 <repo_path> <commit_hash> [output_dir]"
    echo "  repo_path: Git仓库的绝对路径"
    echo "  commit_hash: Commit哈希值"
    echo "  output_dir: 输出目录路径(可选,默认为技能目录下的temp文件夹)"
    exit 1
fi

REPO_PATH="$1"
COMMIT_HASH="$2"

# 验证仓库路径
if [ ! -d "$REPO_PATH" ]; then
    echo "错误: 路径不存在: $REPO_PATH"
    exit 1
fi

if [ ! -d "$REPO_PATH/.git" ]; then
    echo "错误: 不是Git仓库: $REPO_PATH"
    exit 1
fi

# 确定输出目录
if [ $# -ge 3 ]; then
    OUTPUT_DIR="$3"
else
    # 默认使用技能目录下的temp文件夹
    SCRIPT_DIR="$(cd "$(dirname "$0")/.." && pwd)"
    OUTPUT_DIR="$SCRIPT_DIR/temp"
fi

# 创建输出目录
mkdir -p "$OUTPUT_DIR"

# 输出文件路径
OUTPUT_FILE="$OUTPUT_DIR/$COMMIT_HASH.md"

# 切换到仓库目录并获取commit信息
echo "正在获取commit $COMMIT_HASH 的信息..."
cd "$REPO_PATH"

# 写入Markdown文件
{
    echo "# Commit: $COMMIT_HASH"
    echo ""
    echo '```diff'
    git show "$COMMIT_HASH"
    echo '```'
} > "$OUTPUT_FILE"

echo "✓ Commit信息已保存到: $OUTPUT_FILE"
echo "文件路径: $OUTPUT_FILE"
