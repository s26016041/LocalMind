
:: 需要再 windows 環境下執行 並且要填好 setx GITHUB_TOKEN "???"
:: GITHUB_TOKEN 可以去你的 github 找


@REM @echo off
@REM setlocal enabledelayedexpansion
@REM chcp 65001 > nul

@REM echo 正在清理舊的檔案...
@REM if exist build rd /s /q build
@REM if exist dist rd /s /q dist

@REM echo 正在開始封裝 .exe...
@REM pyinstaller --noconsole --onefile --paths=src main.py

@REM if %ERRORLEVEL% neq 0 (
@REM     echo [錯誤] 封裝失敗，請檢查程式碼！
@REM     pause
@REM     exit /b
@REM )

echo 封裝完成！正在檢查版本並準備上傳...

:: 執行版本檢查與上傳邏輯
python src/push.py

pause


