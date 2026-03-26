import os
import subprocess
from ..version import version
import sys

# 匯入你的版本號 (假設 version.py 在 src 下)
try:
    from version import version as local_version
except ImportError:
    # 也可以用讀檔的方式
    with open("src/version.py", "r", encoding="utf-8") as f:
        exec(f.read())
        local_version = version

def run_command(cmd):
    return subprocess.run(cmd, shell=True, capture_output=True, text=True)

def check_and_upload():
    print(f"本地版本: v{local_version}")

    # 1. 獲取 GitHub 最新 Release Tag
    result = run_command("gh release view --json tagName --template \"{{.tagName}}\"")
    remote_version = result.stdout.strip().replace("v", "")

    if local_version == remote_version:
        print("版本一致，無需上傳。")
        return

    print(f"發現新版本！遠端: v{remote_version} -> 本地: v{local_version}")

    # 2. 建立新 Release 並上傳 dist\main.exe
    # --generate-notes 會自動根據 Commit 產生說明
    tag = f"v{local_version}"
    print(f"正在建立 Release {tag} 並上傳檔案...")
    
    upload_cmd = f'gh release create {tag} "dist/main.exe" --title "Release {tag}" --notes "自動封裝上傳"'
    
    upload_result = run_command(upload_cmd)
    
    if upload_result.returncode == 0:
        print("✅ 上傳成功！")
    else:
        print(f"❌ 上傳失敗: {upload_result.stderr}")

if __name__ == "__main__":
    check_and_upload()
