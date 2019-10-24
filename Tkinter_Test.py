import tkinter

#関数
def foo():
    print('Hello, %s!' % t.get())

#GUI初期化
root = tkinter.Tk()
root.title(u"Software Title")
root.geometry("400x300")

#ウィジェットの定義
frame_01 = tkinter.Frame(root)
label_01 = tkinter.Label(frame_01, text = 'Your name:')

t = tkinter.StringVar()

entry_01 = tkinter.Entry(frame_01, textvariable = t)
button_01 = tkinter.Button(frame_01, text = 'OK', command = foo)

#ウィジェットの配置
frame_01.grid(row=0,column=0)
label_01.grid(row=1,column=1)
entry_01.grid(row=1,column=2)
button_01.grid(row=1,column=3)

for child in frame_01.winfo_children():
    child.grid_configure(padx=5, pady=5)

#GUI終了
root.mainloop()
