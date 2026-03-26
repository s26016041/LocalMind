from openrouter import OpenRouter
from src.const import const
import subprocess

API_KEY_ERROR="API key 錯誤或官方API異常，請稍後再試！"

def send_message(message: str)-> str:
    const.AI_MESSAGES.append({"role": "user", "content": message})
    try:
        while True:
            with OpenRouter(
                api_key=const.API_KEY
            ) as client:
                response = client.chat.send(
                    model="openai/gpt-5.4",
                    messages=const.AI_MESSAGES
                )
            ai_reply = response.choices[0].message.content
            print ("AI回覆:", ai_reply)
            const.AI_MESSAGES.append({"role": "assistant", "content": ai_reply})

            if ai_reply.strip().startswith("完成:"):
                return ai_reply.strip().split("完成:")[1].strip()

            process = subprocess.run(
                ai_reply.strip().split("命令:", 1)[1].strip(),
                shell=True, 
                capture_output=True, # 等同於同時設定 stdout=PIPE 和 stderr=PIPE
                text=True,
                encoding='cp950',    # 強制指定 Windows 繁體中文編碼
                errors='replace'     # 【關鍵】遇到解不開的字元不報錯，直接替換成 ?
            )
            stdout, err = process.stdout, process.stderr
            command = stdout + err
            print ("command:", command)

            const.AI_MESSAGES.append({"role": "user", "content":f"執行完畢: {command}"})
    except Exception as e:
        if const.AI_MESSAGES and const.AI_MESSAGES[-1].get("role") == "user":
            const.AI_MESSAGES.pop()
        return API_KEY_ERROR



        
    

def clear_messages():
    const.AI_MESSAGES.clear()
    const.AI_MESSAGES.append(const.SYSTEM)

