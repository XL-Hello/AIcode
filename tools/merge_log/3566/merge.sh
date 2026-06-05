#!/bin/bash
# 遍历当前目录下所有 downlog_dreame-*.tar.gz 文件，
# 解压后找到其中的 log/ 文件夹，合并 .dre.log.tar.gz.n* 生成对应的 downlog_dreame-*.log

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"

# 检查是否存在 downlog_dreame-*.tar.gz 文件
shopt -s nullglob
tar_files=("$SCRIPT_DIR"/downlog_dreame-*.tar.gz)
shopt -u nullglob

if [ ${#tar_files[@]} -eq 0 ]; then
    echo "未找到 downlog_dreame-*.tar.gz 文件"
    exit 1
fi

echo "找到 ${#tar_files[@]} 个 downlog_dreame-*.tar.gz 文件"

for tar_file in "${tar_files[@]}"; do
    basename_tar=$(basename "$tar_file" .tar.gz)
    output="$SCRIPT_DIR/${basename_tar}.log"

    echo "处理: $(basename "$tar_file")"

    tmpdir=$(mktemp -d)

    # 解压 downlog_dreame-*.tar.gz
    tar xzf "$tar_file" -C "$tmpdir" 2>/dev/null

    # 找到解压出的 log/ 文件夹
    log_dir=$(find "$tmpdir" -maxdepth 2 -type d -name "log" | head -1)

    if [ -z "$log_dir" ]; then
        echo "  警告: 未找到 log/ 文件夹，跳过"
        rm -rf "$tmpdir"
        continue
    fi

    # 清空输出文件
    > "$output"

    # 按文件名中的时间戳排序，依次解压 .dre.log.tar.gz.n* 并合并
    ls "$log_dir"/*.dre.log.tar.gz.n* 2>/dev/null | sort -t/ -k2 | while read -r archive; do
        inner_tmpdir=$(mktemp -d)
        tar xzf "$archive" -C "$inner_tmpdir" 2>/dev/null
        find "$inner_tmpdir" -type f -name '*.dre.log' | sort | while read -r logfile; do
            cat "$logfile" >> "$output"
        done
        rm -rf "$inner_tmpdir"
    done

    line_count=$(wc -l < "$output")
    echo "  输出: $(basename "$output") ($line_count 行)"

    rm -rf "$tmpdir"
done

echo "全部完成"
