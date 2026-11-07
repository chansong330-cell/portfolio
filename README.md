# SONG｜剪輯作品集

沿用原作品集的深色配色、大字首頁、作品分類、卡片、聯絡二維碼與手機版排版。訪客不需要登入即可查看。

- 網頁：GitHub Pages，`main` 分支的根目錄。
- 影片：只放 Releases 附件，不提交到程式碼倉庫。
- 17 支影片：統一存放於 `videos-v1` Release，MP4 H.264／AAC，支援網頁直接播放。
- 網站資料：`portfolio.json`。

## 更新作品

1. 在 Releases 中建立或編輯影片版本，附加自己的 MP4（H.264／AAC）或 WebM，完成後發布。
2. 複製附件原始連結，例如 `https://github.com/chansong330-cell/portfolio/releases/download/videos-v1/national-year-end.mp4`。不要保存重新導向後帶短期簽名的網址。
3. 在網站「作品管理」頁整理作品草稿並下載 `portfolio.json`，或直接在 GitHub 編輯現有 JSON。
4. 將更新的 `portfolio.json` 上傳到倉庫根目錄，取代原檔並提交。等 Pages 部署完成，公開網站即更新。
5. 封面圖片可以放在倉庫根目錄；資料填 `./cover.jpg`。新增影片請保持獨特的作品 id。

管理頁是本機草稿編輯器，不會自動授權或寫入 GitHub。公開訪客不能藉由此頁修改倉庫。不要在前端放 Token、密碼或 API Key。

## 開啟 Pages

Settings → Pages → Deploy from a branch → main → /(root) → Save。

## 播放與存取

使用 HTML5 影片播放器，點擊作品後才載入影片，支援 `?work=作品id` 分享連結。Releases 並非具有影片串流 SLA 的服務，播放與拖曳效果需要實測。GitHub Pages 與 Releases 在中國大陸的可達性不能保證。

17 支影片均已從原始作品集資料夾轉檔、壓縮或重新封裝。上傳後核對檔案大小與 SHA-256；原始檔案未修改。
