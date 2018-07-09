from tkinter import*
import tkinter.messagebox
from PIL import Image, ImageTk
from socket_png import img as socket
import base64
import os

root=tkinter.Tk()
# 引用代码化的背景图片
tmp = open('socket.png', 'wb')
tmp.write(base64.b64decode(socket))
tmp.close()
# 主界面初始化
root.title("一个诚意满满的男生呢")
root.geometry("500x300")
root.geometry("+500+200")
root.resizable(0,0)
canvas=Canvas(root,width=500,height=300,bg='white')
image=Image.open("socket.png")
# image.show() 测试
# 插入背景图
im=ImageTk.PhotoImage(image)
canvas.create_image(250,150,image=im)
canvas.pack()
# 窗口关闭警告
def closeWindow():
    tkinter.messagebox.showerror(title="警告",message= "不许关闭,好好回答!")
    return
root.protocol('WM_DELETE_WINDOW',closeWindow)
# 设置文字
lable1 = Label(root, text="肖自胜", font=("Arial", 14))
lable2 = Label(root, text="我们晚上去散步吧！", font=("Arial", 24))
lable1.place(x=210,y=50,anchor='nw')
lable2.place(x=120,y=100,anchor='nw')

# photo = PhotoImage(file="one.gif")
# theLabel = Label(root,text='',image=photo,compound =CENTER,font=("华文行楷",20),fg = "white")
# photo = PhotoImage(file='one.gif')
# imgLabel = Label(root, imag=photo)
# imgLabel.pack()

# def call_back(event):                                      # 添加动作部分
#    print("location",event.x_root,event.y_root)
# def check_mouse():
#    frame=Frame(root,width=500,height=300,background='green')
#    frame.bind("<Motion>",call_back())
#    frame.pack()
#    frame.focus_set()

#   跳转最终页 Flower 未插入背景图 限制使用
def Flower():
    flower = Toplevel(root)
    flower.geometry('200x200')
    flower.resizable(0,0)
    flower.title("with you ")
    btn_f = Button(flower, text="OK  OK ",bg='pink')
    btn_f.config(command=lambda:closeall())  # 调试
    btn_f.place(x=80,y=80,anchor='nw')
    # 加载图片
    # close_agee()

def Belover():
    belover = Toplevel(root)
    belover.geometry('300x200')
    belover.resizable(0, 0)
    belover.title("mamihlapinatapai")
    lable = Label(belover, text="就明晚八点半见咯！", font=("Arial", 24))
    btn = Button(belover, text="嗯嗯，好的呢",bg='pink')
    btn.config(command=lambda: closeall())# 调试
    lable.pack()
    btn.pack()

def Love():
    love = Toplevel(root)
    love.geometry('300x200')
    # love.resizable(0, 0)

    canvas_yes = Canvas(love, width=300, height=200, bg='white')
    image_yes = Image.open("yes.png")
    # image_yes.show()
    im_yes = ImageTk.PhotoImage(image_yes)
    canvas_yes.create_image(300,200,image=im_yes)
    canvas_yes.place(x=0,y=0,anchor='nw')

    # photo = root.PhotoImage(file="yes.png")
    # thelabel = love.label(love,text="hello ",justify=love.LEFT,image=photo,compound=love.CENTER,font=('华文行楷',20),fg='white')
    # thelabel.pack()


    love.title("很高兴了呢")
    lable = Label(love,text="--现在如何呢--", font=("Arial", 18))
    btn = Button(love, text="好像不行耶")
    btn.config(command=lambda :Belover())
    lable.pack()
    love.protocol('WM_DELETE_WINDOW',closenolove)
    btn.pack()
# 点击不喜欢的操作

def NoLove():
    no_love = Toplevel(root)
    no_love.geometry('300x200')
    no_love.resizable(0, 0)
    no_love.title("再考虑考虑呗")
    lable = Label(no_love,text="再考虑考虑呗", font=("Arial", 24))
    btn_y = Button(no_love, text="嗯，好的")
    btn_y.config(command=lambda :closenolove(no_love))
    btn_n = Button(no_love, text="嗯，不行")
    btn_n.config(command=lambda: Nolove_sheet_1())
    lable.pack()
    btn_y.pack()
    btn_n.pack()

def Nolove_sheet_1():
    no_love_sheet_1 = Toplevel(root)
    no_love_sheet_1.geometry('300x200')
    no_love_sheet_1.resizable(0, 0)
    no_love_sheet_1.title("再考虑考虑呗")
    lable = Label(no_love_sheet_1, text="不行？？ 不存在的啦", font=("Arial", 20))
    btn_y_1 = Button(no_love_sheet_1, text="嗯，好的")
    btn_y_1.config(command=lambda: Belover())  # 调试
    btn_n_1 = Button(no_love_sheet_1, text="嗯，不行")
    btn_n_1.config(command=lambda: Nolove_sheet_2())
    lable.pack()
    btn_y_1.pack()
    btn_n_1.pack()

def Nolove_sheet_2():
    no_love_sheet_2 = Toplevel(root)
    no_love_sheet_2.geometry('300x200')
    no_love_sheet_2.resizable(0, 0)
    no_love_sheet_2.title("再考虑考虑呗")
    lable = Label(no_love_sheet_2, text="是 真的 真的 嘛 ", font=("Arial", 20))
    btn_y_2 = Button(no_love_sheet_2, text="嗯，好的")
    btn_y_2.config(command=lambda: Belover())  # 调试
    btn_n_2 = Button(no_love_sheet_2, text="嗯，不行")
    btn_n_2.config(command=lambda:Nolove_sheet_3())
    lable.pack()
    btn_y_2.pack()
    btn_n_2.pack()

def Nolove_sheet_3():
    no_love_sheet_3 = Toplevel(root)
    no_love_sheet_3.geometry('300x200')
    no_love_sheet_3.resizable(0, 0)
    no_love_sheet_3.title("再考虑考虑呗")
    lable = Label(no_love_sheet_3, text="不信 不信  不信 ", font=("Arial", 24))
    btn_y_3 = Button(no_love_sheet_3, text="嗯，好的")
    btn_y_3.config(command=lambda: Belover())  # 调试
    btn_n_3 = Button(no_love_sheet_3, text="嗯，不行")
    btn_n_3.config(command=lambda: Nolove_sheet_4())
    lable.pack()
    btn_y_3.pack()
    btn_n_3.pack()

def Nolove_sheet_4():
    no_love_sheet_4 = Toplevel(root)
    no_love_sheet_4.geometry('300x200')
    no_love_sheet_4.resizable(0, 0)
    no_love_sheet_4.title("再考虑考虑呗")
    lable = Label(no_love_sheet_4, text="那就在楼下等你咯", font=("Arial", 24))
    btn_y_4 = Button(no_love_sheet_4, text="嗯，好的")
    btn_y_4.config(command=lambda: Belover())  # 调试
    btn_n_4 = Button(no_love_sheet_4, text="嗯，不行")
    btn_n_4.config(command=lambda: Nolove_sheet_1())
    lable.pack()
    btn_y_4.pack()
    btn_n_4.pack()

# 子窗口关闭操作
def closeall():
    root.destroy()
def closelove(no_love):
    root.destroy()
    love.destroy()
def closenolove(no_love):
    no_love.destroy()
    pass
def close_agee():
    lover.destroy()

# 设置 主界面 按钮
btn1 = Button(root, text="好的呢",activebackground='white')
# 配置按钮
btn1.config(command=Love)
btn2 = Button(root, text="不行",activebackground='white')
btn2.config(command=NoLove)
# 调用tkinter的布局管理模块
btn1.place(x=50,y=210,anchor='nw')
btn2.place(x=420,y=210,anchor='nw')
# 删除可执行文件生成的临时图片
os.remove("socket.png")

root.mainloop()
