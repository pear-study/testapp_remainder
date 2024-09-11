import tkinter as tk
import os
import datetime


#ファイル操作の定義
def save_task():
    task1 = text1.get("1.0","end-1c")
    if task1:
        with open("task_list.txt","w") as file:
            file.write(task1)
    window.destroy()

def open_task():
    if not os.path.exists("task_list.txt"):
        with open("task_list.txt","w"):
            pass
    with open("task_list.txt","r") as file:
        task1 = file.read()
    text1.delete("1.0","end")
    text1.insert("1.0",task1)

def clear_task():
    text1.config(bg = "#99ff99")
    check_button.config(text = "済")

window = tk.Tk() #ウィンドウを作成
window.title("リマインダー") #タイトル設定

window.geometry("400x400") #ウィンドウサイズを変更
main_color = "#dcdcdc" #グローバルカラーの設定
window.config(bg = main_color) #ウィンドウ背景色の設定

frame1 = tk.Frame(window)
frame1.pack(pady = 20)

dt = datetime.datetime.today() #現在時刻の取得
date = tk.Label(frame1,text = str(dt.date()), font = "メイリオ") #現在の年月日の出力
date.pack()

frame2 = tk.Frame(window)
frame2.pack()

check_button = tk.Button(frame2, text = "未", command = clear_task) #ステータスボタンの設置
check_button.grid(row = 0,column = 0)
text1 = tk.Text(frame2,height = 1, width = 30,bg ="#ff9999") #テキストボックスの設置
text1.grid(row = 0, column = 1)

open_task() #保存したタスクを読み取る

window.protocol("WM_DELETE_WINDOW",save_task) #ウィンドウを閉じるときにタスクを保存する

window.mainloop()