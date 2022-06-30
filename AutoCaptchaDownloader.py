import tkinter as tk                   #匯入tkinter模組
from PIL import ImageTk,Image
from tkinter.filedialog import askopenfilename #Cchrome Driver下載路徑選擇元件
from tkinter import messagebox
import catch_picture

win = tk.Tk()                          # 建立主視窗物件
win.geometry('480x500')                # 設定主視窗預設尺寸為480x500
win.resizable(False,False)             # 設定主視窗的寬跟高皆不可縮放
win.title('Captch Parser')  # 設定主視窗標題
win.iconbitmap('./parser_icon.ico')          # 設定主視窗 icon

img = Image.open("./folder.png")
img = ImageTk.PhotoImage(img)
imLabel=tk.Label(win,image=img)
imLabel.pack()

def Area(var,label,text_var):
    #設定URL輸入區域
    var = tk.Frame(win, width=640, height=50)
    var.pack()
    #設定提示文字
    lb = tk.Label(var, text=label,fg='black')
    lb.place(rely=0.2, relx=0.05)
    # 取得輸入的網址
    text_var = tk.StringVar()
    input_et = tk.Entry(var, bd=2, width=43, textvariable=text_var)
    input_et.place(rely=0.2, relx=0.3)

    return text_var

def select_path():
    path_ = askopenfilename()
    var_path_text.set(path_)
global flag
flag = 0
def get_value():
    global flag
    URL = f1.get()
    xpath = f2.get()
    folder_name = f3.get()
    number = int(f4.get())
    var_path_text = f5.get()
    times = float(f6.get())
    print(var_path_text,URL,xpath,folder_name,number,times)
    catch_picture.catch_picture(var_path_text,URL,xpath,folder_name,number,times)

    messagebox.showinfo('Misson Completed!', 'Done')

choice_frm = tk.Frame(win, width=640, height=50)
choice_frm.pack()
#設定提示文字
label_path = tk.Label(choice_frm, text='Driver Path：', cursor='xterm')
label_path.place(rely=0,relx=0.05)
var_path_text = tk.StringVar()
#設定路徑輸入框
entry_path = tk.Entry(choice_frm, bd=2, width=43, textvariable=var_path_text, cursor='xterm')
entry_path.place(rely=0,relx=0.21)
#設定改變路徑按鈕
button_choice = tk.Button(choice_frm, text='select', bd=1, width=6, command=select_path, cursor='hand2')
button_choice.place(rely=0,relx=0.87)

f1 = Area('f1','Web Site URL：','url')
f2 = Area('f2','Image Xpath：','xpath')
f3 = Area('f3','Save Folder Name：','folder_name')
f4 = Area('f4','Crawler Number：','number')
f5 = var_path_text
f6 = Area('f6','Times Wait Catch：','times')

submit = tk.Frame(win, width=640, height=50)
submit.pack()
#設定改變路徑按鈕
button_choice = tk.Button(submit, text='S U B M I T', bd=4, width=12, command=get_value, cursor='hand2')
button_choice.place(rely=0.2,relx=0.75)

win.mainloop()
win.quit()