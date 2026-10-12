from openrouter import OpenRouter
from src.const import const
import subprocess
import re

API_KEY_ERROR="API key 錯誤或官方API異常，請稍後再試！"
MODEL = "google/gemini-3.1-flash-lite-preview"
MAX_STEPS = 10  # 一次對話最多讓 AI 執行幾個命令，避免無限迴圈一直扣 API 費用

# AI 回覆格式：「命令:xxx」或「完成:xxx」，冒號全形半形都接受
REPLY_PATTERN = re.compile(r"^(命令|完成)\s*[:：]\s*(.*)$", re.DOTALL)


def _ask_ai(messages) -> str:
    with OpenRouter(
        api_key=const.API_KEY
    ) as client:
        response = client.chat.send(
            model=MODEL,
            messages=messages
        )
    return response.choices[0].message.content


def _run_command(command: str):
    process = subprocess.run(
        command,
        shell=True,
        capture_output=True, # 等同於同時設定 stdout=PIPE 和 stderr=PIPE
        text=True,
        encoding='cp950',    # 強制指定 Windows 繁體中文編碼
        errors='replace'     # 【關鍵】遇到解不開的字元不報錯，直接替換成 ?
    )
    return process.returncode, process.stdout + process.stderr


def send_message(message: str, confirm_command=None) -> str:
    """
    confirm_command: 執行命令前呼叫，傳入命令字串，回傳 True 才會執行。
                     沒給的話一律不執行命令。
    """
    const.AI_MESSAGES.append({"role": "user", "content": message})

    for _ in range(MAX_STEPS):
        try:
            ai_reply = _ask_ai(const.AI_MESSAGES)
        except Exception as e:
            print("呼叫 API 發生錯誤:", e)
            if const.AI_MESSAGES and const.AI_MESSAGES[-1].get("role") == "user":
                const.AI_MESSAGES.pop()
            return API_KEY_ERROR

        print ("AI回覆:", ai_reply)
        const.AI_MESSAGES.append({"role": "assistant", "content": ai_reply})

        match = REPLY_PATTERN.match((ai_reply or "").strip())
        if match is None:
            return f"AI 回覆的格式不對，沒有執行任何命令：\n{ai_reply}"

        kind, content = match.group(1), match.group(2).strip()
        if kind == "完成":
            return content

        if confirm_command is None or not confirm_command(content):
            const.AI_MESSAGES.append({"role": "user", "content": f"使用者拒絕執行命令：{content}"})
            return f"已取消，沒有執行命令：{content}"

        returncode, output = _run_command(content)
        status = "成功" if returncode == 0 else "失敗"
        print (f"command ({status}, returncode={returncode}):", output)

        const.AI_MESSAGES.append({"role": "user", "content":f"執行{status} (returncode={returncode}): {output}"})

    return f"已經執行了 {MAX_STEPS} 個命令還沒完成，先停下來避免無限執行。可以再傳一次訊息讓 AI 繼續。"


def check_api_key() -> bool:
    """只送一則測試訊息確認 API Key 能用，不影響目前的對話紀錄，也不執行任何命令"""
    try:
        _ask_ai([const.SYSTEM, {"role": "user", "content": "嗨!"}])
        return True
    except Exception as e:
        print("API key 驗證失敗:", e)
        return False


def clear_messages():
    const.AI_MESSAGES.clear()
    const.AI_MESSAGES.append(const.SYSTEM)
