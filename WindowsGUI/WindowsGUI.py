import tkinter as tk
from tkinter import Tk
from tkinter import messagebox
# 创建对象root
root = Tk()
root["bg"]="black"              # 设置背景颜色
root.attributes("-alpha", 0.6)  # 设置窗体虚化程度，数字越小虚化程度越高
root.title('说出你的真心话')     # 设置窗口标题
root.geometry('500x400')        # 设置窗体的大小(宽高),可以采用默认


def show_questions(name, myname):
    while(1):                   # 持续弹窗
        result = tk.messagebox.askquestion("在你的心目中", f"{myname}是不是最帅的?", icon='warning')
        if(result=='yes'):      # 判断用户选项
            # 通过config()重新设置窗体内容,通过font设置字体样式，fg设置字体色，bg设置背景色
            lb.config(text=f'不,{name}, 你才是最帅的！', fg='white', bg='black', font=('Times', 16, 'bold'))
            break               #退出循环
        else:
            lb.config(text=f"{name},你摸着自己的良心再好好想想!!!", fg='red', bg='black', font=('Times', 16, 'bold'))


myname = 'PeakofMountains'   # 填上自己的姓名

# 创建一个Label组件，每个组件都有一些属性可以设置比如宽高字体颜色
lb = tk.Label(root, text='\n Welcome to magic mirror \n\nPlease input your name', width=40, height=10, bg='black', fg='white' ,font=('Times', 20, 'bold'))
lb.pack(side='top', padx=5)   # 将Label组件通过pack()塞到窗口中去,side有4中选择：top、bottom 、left、right

# 添加文本输入框可以使用 Entry 对象
text = tk.Entry(root, width=10)     # 设置输入框的长度
text.pack()

# 加个按钮，可以使用 command 来绑定回调函数,用get()得到Entry输入内容
bt = tk.Button(text='OK', width=10, bg='burlywood', fg='black', font=('Times', 13, 'bold'), command=lambda: show_questions(text.get(), myname))
bt.pack(side='bottom', padx=5)   # 每个组件都要用对象调用pack()将其内容塞到窗口中

# 循环执行，接受用户的数据输入
tk.mainloop()