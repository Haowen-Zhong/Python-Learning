'''
bottom组件
'''
from tkinter import *

def callback():
	var.set("吹吧你，我才不信呢！")

root = Tk()
frame1 = Frame(root)
frame2 = Frame(root)

var = StringVar()
var.set("您所下载的内容需要高等广义相对论的知识，\n您暂时无法学习")

textLabel = Label(frame1,textvariable = var,
				  justify=LEFT)
textLabel.pack(side = LEFT)

photo = PhotoImage(file="p2.gif")
imgLabel = Label(frame1,image=photo)
imgLabel.pack(side = RIGHT)

theButtom = Button(frame2,text = "我已经学习过相关前置知识，可以继续学习",command = callback)
theButtom.pack()
frame1.pack(padx = 10,pady = 10)
frame2.pack(padx = 10,pady = 10)
mainloop()

