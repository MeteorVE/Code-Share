# FFmpeg

- 將音樂檔案和 jpg 合成一個影片
  - -vf scale=720:1024 是當時那張照片更適合這個大小，它被要求是 4 的倍數。

```sh
ffmpeg -i input.jpg -i input.flac -c:v libx265 -preset medium -x265-params crf=23 -c:a flac -pix_fmt yuv420p -vf scale=720:1024 -shortest output.mkv
```



- 合併 acc 和 ts 文件

```sh
#!/bin/bash

# 設定資料夾路徑
folder_path="/path/to/your/folder/"

# 創建一個暫存目錄用於存放合併後的.ts和.aac文件
temp_dir=$(mktemp -d)

# 使用find查找以_1080_*.ts結尾的.ts文件並將它們按名稱排序
ts_files=($(find "$folder_path" -type f -name "*_1080_*.ts" | sort))

# 使用find查找以_1080_*.aac結尾的.aac文件並將它們按名稱排序
aac_files=($(find "$folder_path" -type f -name "*_1080_*.aac" | sort))

# 定義一個輔助函數，從文件名中提取數字部分
get_number() {
    local filename="$1"
    echo "$filename" | grep -oE '[0-9]+'
}

# 遍歷.ts文件，對於每個.ts文件，查找對應的.aac文件，如果找到就合併它們
for ts_file in "${ts_files[@]}"; do
    ts_number=$(get_number "$ts_file")
    aac_file="${folder_path}/your_prefix_${ts_number}.aac"

    if [ -f "$aac_file" ]; then
        output_file="$temp_dir/merged_${ts_number}.mp4"
        ffmpeg -i "$ts_file" -i "$aac_file" -c:v copy -c:a aac -strict experimental "$output_file"
    fi
done

# 將所有片段合併成一個.mp4文件
output_file="${1:-output.mp4}"
ffmpeg -f concat -safe 0 -i <(for f in "$temp_dir"/merged_*.mp4; do echo "file '$f'"; done) -c:v copy -c:a aac -strict experimental "$output_file"

# 刪除暫存目錄及其內容
rm -rf "$temp_dir"

echo "合併完成，輸出為 $output_file"
```



