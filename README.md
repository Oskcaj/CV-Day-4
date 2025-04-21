# Superman's CV - Interactive Resume Application

這是一個使用 Streamlit 建立的互動式履歷表應用程序，具有現代化的設計和超人主題的配色方案。

## 功能特點

- 🎨 現代化且響應式的設計
- 💼 完整的個人資料展示
- 🏢 詳細的工作經驗時間軸
- 📚 教育背景
- 💡 專案展示
- 📜 證照認證
- 🌐 語言能力
- 🎯 核心技能展示
- 🏆 專業成就
- 👤 個人照片展示

## 系統要求

- Python 3.8 或更高版本
- pip（Python 包管理器）

## 安裝步驟

1. 克隆此專案：
   ```bash
   git clone <repository-url>
   cd <project-directory>
   ```

2. 創建並啟動虛擬環境（建議）：
   ```bash
   python -m venv venv
   source venv/bin/activate  # Unix/macOS
   # 或
   .\venv\Scripts\activate  # Windows
   ```

3. 安裝依賴包：
   ```bash
   pip install -r requirements.txt
   ```

## 使用方法

1. 確保您已經安裝所有依賴包。

2. 在專案根目錄下運行應用程序：
   ```bash
   streamlit run app.py
   ```

3. 應用程序將在您的默認瀏覽器中自動打開，通常是在 http://localhost:8501

## 自定義內容

1. 個人資料：
   - 編輯 `sample_cv.json` 文件來更新您的個人資訊
   - 支持的字段包括：個人信息、工作經驗、教育背景、技能、專案等

2. 個人照片：
   - 將您的照片放在 `images` 目錄下
   - 命名為 `superman_glasses.jpg`

## 文件結構

```
.
├── app.py              # 主應用程序文件
├── sample_cv.json      # CV 數據文件
├── requirements.txt    # 項目依賴
├── README.md          # 項目文檔
└── images/            # 圖片目錄
    └── superman_glasses.jpg
```

## 技術棧

- Streamlit：用於建立網頁應用界面
- Python：後端邏輯處理
- PIL (Pillow)：圖片處理
- JSON：數據存儲格式

## 注意事項

- 請確保所有圖片都放在正確的目錄中
- JSON 文件格式必須正確，否則可能導致應用程序無法正常運行
- 建議使用虛擬環境來管理依賴包

## 貢獻指南

歡迎提交 Pull Requests 來改進這個項目！請確保您的代碼符合以下要求：

1. 遵循 PEP 8 編碼規範
2. 提供適當的文檔說明
3. 確保所有測試都能通過

## 授權

MIT License
