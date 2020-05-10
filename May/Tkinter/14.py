from tkinter import *

master = Tk()

def test1():
	if e1.get() =="浩文哥":
		print("非常棒！正确！")
		return True
	else:
		print("错误！")
		e1.delete(0,END)
		return False
def test2():
	print("嘤嘤嘤！！！")
	return False
v = StringVar()

e1 = Entry(master,textvariable = v,validate = "focusout",validatecommand = test1,invalidcommand=test2)
e2 = Entry(master)
e1.pack(padx = 10, pady = 10)
e2.pack(padx = 10, pady = 10)

mainloop()
import PyQt5