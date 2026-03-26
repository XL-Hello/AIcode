#!/usr/bin/env bash
set -euo pipefail

# Merge dre/audio logs from nested zips in chronological order.
# Usage:
#   ./merge_rtos_logs.sh [zip_path] [output_dir]

script_dir="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
zip_path="${1:-${script_dir}/log_rtos.zip}"
out_dir="${2:-$(pwd)}"

audio_output="${out_dir}/audio.log"
dre_output="${out_dir}/dre.log"

if [[ ! -f "$zip_path" ]]; then
  echo "ERROR: zip file not found: $zip_path" >&2
  exit 1
fi

if ! command -v unzip >/dev/null 2>&1; then
  echo "ERROR: unzip command not found" >&2
  exit 1
fi

if ! command -v tar >/dev/null 2>&1; then
  echo "ERROR: tar command not found" >&2
  exit 1
fi

mkdir -p "$out_dir"

tmp_dir=$(mktemp -d)
cleanup() {
  rm -rf "$tmp_dir"
}
trap cleanup EXIT

outer_dir="$tmp_dir/outer"
mkdir -p "$outer_dir"

# Step 1: unzip outer archive.
unzip -q "$zip_path" -d "$outer_dir"

# Step 2: collect and sort inner zip files.
mapfile -t inner_zips < <(find "$outer_dir" -type f -name '*.zip' | sort)

if [[ ${#inner_zips[@]} -eq 0 ]]; then
  echo "ERROR: no inner zip files found in $zip_path" >&2
  exit 1
fi

manifest="$tmp_dir/manifest.tsv"
: > "$manifest"

# Step 3: build a sortable manifest of all log archives.
for inner_zip in "${inner_zips[@]}"; do
  while IFS= read -r member; do
    [[ -z "$member" ]] && continue

    base=$(basename "$member")
    kind=""

    if [[ "$base" =~ \.audio_dre\.log\.tar\.gz$ ]]; then
      kind="audio"
      if [[ "$base" =~ _([0-9]{15})\.audio_dre\.log\.tar\.gz$ ]]; then
        ts_key="${BASH_REMATCH[1]}"
      elif [[ "$base" =~ ^([0-9]{14}) ]]; then
        ts_key="${BASH_REMATCH[1]}"
      else
        ts_key="$base"
      fi
    elif [[ "$base" =~ \.dre\.log\.tar\.gz$ ]]; then
      kind="dre"
      if [[ "$base" =~ _([0-9]{15})\.dre\.log\.tar\.gz$ ]]; then
        ts_key="${BASH_REMATCH[1]}"
      elif [[ "$base" =~ ^([0-9]{14}) ]]; then
        ts_key="${BASH_REMATCH[1]}"
      else
        ts_key="$base"
      fi
    else
      continue
    fi

    printf '%s\t%s\t%s\t%s\n' "$ts_key" "$kind" "$inner_zip" "$member" >> "$manifest"
  done < <(unzip -Z1 "$inner_zip")
done

# Step 4: merge by chronological order per kind.
: > "$audio_output"
: > "$dre_output"

audio_count=0
dre_count=0

while IFS=$'\t' read -r ts_key kind inner_zip member; do
  [[ -z "$kind" ]] && continue

  if [[ "$kind" == "audio" ]]; then
    unzip -p "$inner_zip" "$member" | tar -xzO >> "$audio_output"
    audio_count=$((audio_count + 1))
  elif [[ "$kind" == "dre" ]]; then
    unzip -p "$inner_zip" "$member" | tar -xzO >> "$dre_output"
    dre_count=$((dre_count + 1))
  fi
done < <(sort -t $'\t' -k2,2 -k1,1 -k4,4 "$manifest")

echo "Done."
echo "  audio merged files: $audio_count -> $audio_output"
echo "  dre merged files:   $dre_count -> $dre_output"
