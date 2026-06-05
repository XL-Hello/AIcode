#!/bin/bash
# RTOS merge.sh - 遍历当前目录下所有zip文件，按时间序列解压并合并日志
#
# 处理流程（对每个顶层 zip）：
#   1. 解压 zip 到临时目录
#   2. 优先按时间序列解压所有嵌套 *.zip 文件
#   3. 合并 *.audio_dre.log.tar_*.gz 分片 → <zip名>_audio.log
#   4. 合并 *.dre.log.tar_*.gz 分片        → <zip名>.log
#   5. 合并 *.dre.log（单体日志）           → <zip名>.log
#   6. 合并 *.audio_dre.log（单体日志）     → <zip名>_audio.log

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"

# ===================== 查找 zip 文件 =====================
shopt -s nullglob
zip_files=("$SCRIPT_DIR"/*.zip)
shopt -u nullglob

if [ ${#zip_files[@]} -eq 0 ]; then
    echo "未找到 *.zip 文件"
    exit 1
fi

echo "找到 ${#zip_files[@]} 个 zip 文件"

# 按文件名排序（时间序列体现在文件名中）
IFS=$'\n' sorted_zips=($(sort <<<"${zip_files[*]}")); unset IFS

# ===================== 辅助函数 =====================

# 在目录中按模式查找文件，结果存入全局数组 FOUND_FILES
find_files() {
    local dir="$1"
    local pattern="$2"
    shift 2
    local extra_args=("$@")
    FOUND_FILES=()
    while IFS= read -r f; do
        FOUND_FILES+=("$f")
    done < <(find "$dir" -name "$pattern" -type f "${extra_args[@]}" 2>/dev/null | sort)
}

# ===================== 主处理循环 =====================

for zip_file in "${sorted_zips[@]}"; do
    zip_base=$(basename "$zip_file" .zip)
    output_log="$SCRIPT_DIR/${zip_base}.log"
    output_audio="$SCRIPT_DIR/${zip_base}_audio.log"

    echo ""
    echo "========== 处理: $(basename "$zip_file") =========="

    tmpdir=$(mktemp -d)

    # 解压顶层 zip
    unzip -o "$zip_file" -d "$tmpdir" 2>/dev/null

    # ---- Step 1: 按时间序列解压所有嵌套 *.zip ----
    find_files "$tmpdir" "*.zip"
    nested_zips=("${FOUND_FILES[@]}")

    if [ ${#nested_zips[@]} -gt 0 ]; then
        echo "  [1/5] 找到 ${#nested_zips[@]} 个嵌套 zip，按时间序列解压..."
        for nz in "${nested_zips[@]}"; do
            echo "        - $(basename "$nz")"
            unzip -o "$nz" -d "$tmpdir" 2>/dev/null
        done
    else
        echo "  [1/5] 无嵌套 zip"
    fi

    # 初始化输出文件
    > "$output_log"
    > "$output_audio"

    # ---- Step 2: 合并 *.audio_dre.log.tar_*.gz → _audio.log ----
    find_files "$tmpdir" "*.audio_dre.log.tar_*.gz"
    audio_tar_logs=("${FOUND_FILES[@]}")

    if [ ${#audio_tar_logs[@]} -gt 0 ]; then
        echo "  [2/5] 合并 ${#audio_tar_logs[@]} 个 audio_dre.log.tar_*.gz → ${zip_base}_audio.log"
        for archive in "${audio_tar_logs[@]}"; do
            inner_tmp=$(mktemp -d)
            tar xzf "$archive" -C "$inner_tmp" 2>/dev/null
            find "$inner_tmp" -type f -name '*.audio_dre.log' -exec cat {} + >> "$output_audio" 2>/dev/null
            rm -rf "$inner_tmp"
        done
    else
        echo "  [2/5] 无 audio_dre.log.tar_*.gz"
    fi

    # ---- Step 3: 合并 *.dre.log.tar_*.gz → .log（排除 audio_dre） ----
    find_files "$tmpdir" "*.dre.log.tar_*.gz" ! -name '*.audio_dre.log.tar_*.gz'
    dre_tar_logs=("${FOUND_FILES[@]}")

    if [ ${#dre_tar_logs[@]} -gt 0 ]; then
        echo "  [3/5] 合并 ${#dre_tar_logs[@]} 个 dre.log.tar_*.gz → ${zip_base}.log"
        for archive in "${dre_tar_logs[@]}"; do
            inner_tmp=$(mktemp -d)
            tar xzf "$archive" -C "$inner_tmp" 2>/dev/null
            find "$inner_tmp" -type f -name '*.dre.log' ! -name '*.audio_dre.log' -exec cat {} + >> "$output_log" 2>/dev/null
            rm -rf "$inner_tmp"
        done
    else
        echo "  [3/5] 无 dre.log.tar_*.gz"
    fi

    # ---- Step 4: 合并单体 *.dre.log → .log（排除 audio_dre） ----
    find_files "$tmpdir" "*.dre.log" ! -name '*.audio_dre.log'
    dre_logs=("${FOUND_FILES[@]}")

    if [ ${#dre_logs[@]} -gt 0 ]; then
        echo "  [4/5] 合并 ${#dre_logs[@]} 个 .dre.log → ${zip_base}.log"
        for f in "${dre_logs[@]}"; do
            cat "$f" >> "$output_log"
        done
    else
        echo "  [4/5] 无 .dre.log"
    fi

    # ---- Step 5: 合并单体 *.audio_dre.log → _audio.log ----
    find_files "$tmpdir" "*.audio_dre.log"
    audio_dre_logs=("${FOUND_FILES[@]}")

    if [ ${#audio_dre_logs[@]} -gt 0 ]; then
        echo "  [5/5] 合并 ${#audio_dre_logs[@]} 个 .audio_dre.log → ${zip_base}_audio.log"
        for f in "${audio_dre_logs[@]}"; do
            cat "$f" >> "$output_audio"
        done
    else
        echo "  [5/5] 无 .audio_dre.log"
    fi

    # ===================== 输出统计 =====================
    log_lines=$(wc -l < "$output_log" 2>/dev/null || echo 0)
    audio_lines=$(wc -l < "$output_audio" 2>/dev/null || echo 0)
    log_size=$(du -h "$output_log" 2>/dev/null | cut -f1)
    audio_size=$(du -h "$output_audio" 2>/dev/null | cut -f1)

    echo "  ---- 输出 ----"
    echo "  ${zip_base}.log:       $log_lines 行 ($log_size)"
    echo "  ${zip_base}_audio.log: $audio_lines 行 ($audio_size)"

    rm -rf "$tmpdir"
done

echo ""
echo "========== 全部完成 =========="
