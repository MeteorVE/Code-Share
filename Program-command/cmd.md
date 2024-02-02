# 紀錄一些 Program 所使用的 command line 指令



- iCloud Photos Downloader (command line 拉取 iCloud 照片)

  - https://github.com/icloud-photos-downloader/icloud_photos_downloader

  - 以下指令可以下載最近上傳的 50 張照片。

    ```
    icloudpd --directory ./Photos \
    --username your@gmail.com \
    --password your_password \
    --recent 50 \
    ```
- ImageMagick

  ```
  convert input.jpg -resize 100x100 -quality 100 output.jpg
  
  # 指定寬度，但不指定高度、以及指定高度、但不指定寬度
  convert input.jpg -resize 500 output.jpg
  convert input.jpg -resize x500 output.jpg
  ```

  
- End


