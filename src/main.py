import tkinter as tk
from tkinter import scrolledtext

# 1. 建立主視窗
root = tk.Tk()
root.title("我的簡易聊天室")
root.geometry("400x500")

# 2. 建立訊息顯示區 (使用 scrolledtext 可以自動捲動)
chat_display = scrolledtext.ScrolledText(root, state='disabled', width=50, height=20)
chat_display.pack(padx=10, pady=10)

# 3. 定義傳送訊息的邏輯
def send_message():
    message = user_input.get() # 取得輸入框內容
    if message.strip(): # 確保不是空白
        chat_display.config(state='normal') # 開啟編輯權限
        chat_display.insert(tk.END, f"你: {message}\n") # 插入文字
        chat_display.config(state='disabled') # 鎖定唯讀
        user_input.delete(0, tk.END) # 清空輸入框
        chat_display.yview(tk.END) # 自動捲動到底部

# 4. 建立輸入框與按鈕
input_frame = tk.Frame(root)
input_frame.pack(padx=10, pady=5, fill=tk.X)

user_input = tk.Entry(input_frame)
user_input.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(0, 5))
# 綁定 Enter 鍵傳送
user_input.bind("<Return>", lambda event: send_message())

send_button = tk.Button(input_frame, text="傳送", command=send_message)
send_button.pack(side=tk.RIGHT)

# 5. 啟動程式
root.mainloop()