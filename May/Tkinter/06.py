from tkinter import *

root = Tk()
v = IntVar()
c = Checkbutton(root,text = "测试一下啵",variable = v)
c.pack()
l = Label(root,textvariable = v)
#未选中就默认未0，选中为1
l.pack()
mainloop()