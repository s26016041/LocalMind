import tkinter as tk
from tkinter import scrolledtext
from src.geminimind import gemini_mind
from src.const import const


# 1. 建立主視窗
root = tk.Tk()
root.title("本地AI")
root.geometry("400x600")
my_font = ("Microsoft JhengHei", 12)

# 2. 建立訊息顯示區 (使用 scrolledtext 可以自動捲動)
chat_display = scrolledtext.ScrolledText(
    root, 
    state='disabled', 
    width=50, 
    height=20,
    font=my_font,           # <--- 加入這行
    padx=10,                # 讓文字離邊框遠一點，比較美觀
    pady=10
)
chat_display.pack(padx=10, pady=10)

# 3. 定義傳送訊息的邏輯
def send_message():
    message = user_input.get() # 取得輸入框內容
    user_input.delete(0, tk.END) # 清空輸入框
    user_input.config(state='disabled') 
    if message.strip(): # 確保不是空白
        chat_display.config(state='normal') # 開啟編輯權限
        chat_display.insert(tk.END, f"你: {message}\n") # 插入文字
        chat_display.yview(tk.END) # 自動捲動到底部
        chat_display.insert(tk.END, f"等待 AI 回復......\n") # 插入文字
        root.update_idletasks()
        aiMessage=gemini_mind.send_message(message) # 呼叫 gemini_mind 的 send_message 函式
        chat_display.delete("end-2l", "end-1c") 
        chat_display.config(state='disabled') # 鎖定唯讀
        send_ai_message(aiMessage)
    user_input.config(state='normal') 


def send_ai_message(message:str):
    if message.strip(): # 確保不是空白
        chat_display.config(state='normal') # 開啟編輯權限
        chat_display.insert(tk.END, f"AI: {message}\n") # 插入文字
        chat_display.config(state='disabled') # 鎖定唯讀
        chat_display.yview(tk.END) # 自動捲動到底部

def clear_messages():
    const.AI_MESSAGES.clear()
    chat_display.config(state='normal') # 開啟編輯權限
    chat_display.delete(1.0, tk.END) # 清空顯示區
    chat_display.config(state='disabled') # 鎖定唯讀

# 4. 建立輸入框與按鈕
input_frame = tk.Frame(root)
input_frame.pack(padx=10, pady=5, fill=tk.X)

user_input = tk.Entry(
    input_frame, 
    font=my_font
)
user_input.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(0, 5))


clear_button = tk.Button(input_frame, text="清除資料", command=clear_messages)
clear_button.pack(side=tk.RIGHT)



# 綁定 Enter 鍵傳送
user_input.bind("<Return>", lambda event: send_message())

send_button = tk.Button(input_frame, text="傳送", command=send_message)
send_button.pack(side=tk.RIGHT)

# API KEY 輸入框
api_key_frame = tk.Frame(root)
api_key_frame.pack(padx=10, pady=5, fill=tk.X)
api_key_label = tk.Label(api_key_frame, text="API Key:", font=my_font)
api_key_label.pack(side=tk.LEFT, padx=(0, 5))
api_key_input = tk.Entry(
    api_key_frame, 
    font=my_font
)
api_key_input.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(0, 5))
def verify_api_key():
    const.API_KEY=api_key_input.get()
    if gemini_mind.API_KEY_ERROR==gemini_mind.send_message("嗨!"):
        print("API key 錯誤或官方API異常，請稍後再試！")
        return
    print("API key 驗證成功！")
    gemini_mind.clear_messages()


api_key_button = tk.Button(api_key_frame, text="設定API Key",command=verify_api_key )
api_key_button.pack(side=tk.RIGHT)



# 5. 啟動程式
root.mainloop()
