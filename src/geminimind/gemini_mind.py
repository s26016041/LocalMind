from openrouter import OpenRouter
from src.const import const
import requests

API_KEY_ERROR="API key 錯誤或官方API異常，請稍後再試！"

def send_message(message: str)-> str:
    try:
        const.AI_MESSAGES.append({"role": "user", "content": message})
        with OpenRouter(
            api_key=const.API_KEY
        ) as client:
            response = client.chat.send(
                model="anthropic/claude-opus-4.6",
                messages=const.AI_MESSAGES
            )

        const.AI_MESSAGES.append({"role": "assistant", "content": response.choices[0].message.content})
        return response.choices[0].message.content
    except Exception as e:
        return API_KEY_ERROR

def clear_messages():
    const.AI_MESSAGES.clear()

