# LocalMind

> 本地 AI 自動化助手 — 用自然語言讓 AI 幫你執行電腦上的各種任務。

![Platform](https://img.shields.io/badge/Platform-Windows-blue?logo=windows)

---

## ✨ 功能特色

- 🤖 **自然語言對話** — 直接用中文告訴 AI 你想做什麼
- ⚡ **自動執行命令** — AI 自動幫你安裝軟體、查詢系統資訊、管理檔案等
- 🔑 **API Key 一次設定** — 設定後自動記住，下次開啟免重填
- 🆓 **模型** — 預設使用 `google/gemini-3.1-flash-lite-preview`

---

## 📥 下載與安裝

1. 前往 [**Releases 頁面**](https://github.com/<your-username>/LocalMind/releases/latest) 下載最新版的 `main.exe`
2. 將 `main.exe` 放到你想要的資料夾中
3. 雙擊執行即可，**不需要安裝 Python 或任何其他東西**

---

## � 取得 API Key

本程式使用 OpenRouter API，你需要先申請一組免費的 API Key：

1. 前往 [OpenRouter](https://openrouter.ai/) 註冊帳號
2. 進入 [API Keys 頁面](https://openrouter.ai/keys) 建立一組 Key
3. 複製 Key 備用

---

## 🖥️ 使用方式

1. 開啟 `main.exe`
2. 在底部的 **API Key** 欄位貼上你的 Key，點擊「**設定API Key**」
3. 在輸入框中輸入你想做的事，例如：
   - `幫我查看目前系統的 IP 位址`
   - `安裝 Node.js`
   - `列出桌面上所有的 .txt 檔案`
4. 按下「**傳送**」或按 **Enter** 送出
5. AI 會自動完成任務並回覆結果
6. 點擊「**清除資料**」可重置對話紀錄

---

## ⚠️ 注意事項

- 僅支援 **Windows** 系統
- AI 會在你的電腦上執行命令，請留意 AI 的回覆內容
- API Key 儲存在程式同目錄下的 `config.json` 中，請妥善保管

---

## ⚠️ 免責聲明

本專案僅為**個人研究與學習用途**，不提供任何擔保。使用本程式所造成的任何損失或問題，作者概不負責。請自行評估風險後使用。

---

## 📝 授權條款

本專案為個人開發，歡迎自由使用與修改。
