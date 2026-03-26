import os
import subprocess

# 1. 動態讀取 version.py (假設它在專案根目錄)
def get_local_version():
    version_file = "version.py"  # 如果在根目錄
    if not os.path.exists(version_file):
        version_file = "src/version.py" # 如果在 src 裡
        
    variables = {}
    with open(version_file, "r", encoding="utf-8") as f:
        exec(f.read(), variables)
    return variables.get("version", "0.0.0")

# 2. 獲取本地版本
local_version = get_local_version()
print(f"本地版本: v{local_version}")

# 3. 獲取 GitHub 遠端版本
def get_remote_version():
    # 使用 gh 指令獲取最新 tag
    result = subprocess.run("gh release view --json tagName --template \"{{.tagName}}\"", 
                            shell=True, capture_output=True, text=True)
    return result.stdout.strip().replace("v", "")

remote_version = get_remote_version()

# 4. 比對並上傳
if local_version != remote_version:
    tag = f"v{local_version}"
    exe_path = "dist/main.exe"
    
    # 檢查檔案是否存在，避免 gh 指令噴錯
    if not os.path.exists(exe_path):
        print(f"❌ 錯誤：找不到 {exe_path}，請確認 PyInstaller 封裝是否成功。")
    else:
        print(f"🚀 正在建立 GitHub Release {tag} 並上傳 {exe_path}...")
        
        # --generate-notes: 自動根據 git commit 產生說明
        # --title: 設定 Release 的標題
        upload_cmd = f'gh release create {tag} "{exe_path}" --title "Release {tag}" --generate-notes'
        
        result = subprocess.run(upload_cmd, shell=True, capture_output=True, text=True)
        
        if result.returncode == 0:
            print(f"✅ 成功發佈版本 {tag}！")
        else:
            print(f"❌ 上傳失敗，原因：\n{result.stderr}")

else:
    print("版本一致，跳過上傳。")
