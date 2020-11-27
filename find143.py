from Beautifulstring import astring
from tkinter import *
import sys
def get_path():
    try:
        home = [r'.\1.png',r'.\2.png',r'.\3.png']
        sr = astring.name_strs()
        life = False
        for i in home:
            one = sr.cope_fill_name(path=entry.get(), mude='rb')
            onelist = list(one)
            ones = sr.cope_fill_name(path=i,mude='rb')
            frist = list(ones)
            isin = []
            for j in ones:
                for h in onelist:
                    if j == h:
                        isin.append(j)
                    del onelist[0]
                    break
            a = len(isin)
            f = len(frist)
            x = a/f*100
            if x > 90:
                i2 = "这像"+i
                toplevel = Toplevel()
                toplevel.title('人脸识别')
                Label(toplevel,text = i2,fg = 'green').pack()
                life = True
        if not life:
            top = Toplevel()
            top.title('人脸识别')
            Label(top,text = '它不像任何图片').pack()
    except TypeError:
        t = Toplevel()
        t.geometry("200x70")
        t.title('错误')
        def exit():
            t.destroy()
        Label(t,text = '无此图片',font = ('宋体',20),fg = 'red').pack()
        Button(t,text = '确定',command = exit).pack()
if __name__ == '__main__':
    root = Tk()
    root.title('人脸识别')
    e = StringVar()
    l = Label(root,text = '图片路径：',fg = 'red')
    l.grid(row = 1,column = 0)
    entry = Entry(root, textvariable=e, width=30)
    entry.grid(row = 1,column = 1)
    button = Button(root,text = "对比",command = get_path,fg = 'blue')
    button.grid(row = 2,column = 1)
    root.mainloop()
    sys.stdout.write('完毕')