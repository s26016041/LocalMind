@echo off
setlocal enabledelayedexpansion
chcp 65001 > nul

echo 正在清理舊的檔案...
if exist build rd /s /q build
if exist dist rd /s /q dist

echo 正在開始封裝 .exe...
pyinstaller --noconsole --onefile --paths=src main.py

if %ERRORLEVEL% neq 0 (
    echo [錯誤] 封裝失敗，請檢查程式碼！
    pause
    exit /b
)

echo 封裝完成！正在檢查版本並準備上傳...

:: 執行版本檢查與上傳邏輯
python src/push.py

pause
