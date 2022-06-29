import tkinter as tk                   #匯入tkinter模組
from PIL import ImageTk,Image

win = tk.Tk()                          # 建立主視窗物件
win.geometry('480x480')                # 設定主視窗預設尺寸為640x480
win.resizable(False,False)             # 設定主視窗的寬跟高皆不可縮放
win.title('Captch Parser')  # 設定主視窗標題
win.iconbitmap('parser_icon.ico')          # 設定主視窗 icon

img = Image.open("folder.png")
img = ImageTk.PhotoImage(img)
imLabel=tk.Label(win,image=img)
imLabel.pack()

#設定網址輸入區域
input_frm = tk.Frame(win, width=640, height=50)
input_frm.pack()
#設定提示文字
lb = tk.Label(input_frm, text='Type a link like a video or a playlist',fg='black')
lb.place(rely=0.2, relx=0.5, anchor='center')
#設定輸入框
input_url = tk.StringVar()     # 取得輸入的網址
input_et = tk.Entry(input_frm, textvariable=input_url, width=60)
input_et.place(rely=0.75, relx=0.5, anchor='center')

win.mainloop()
win.quit()