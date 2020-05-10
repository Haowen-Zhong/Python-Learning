from tkinter import *

root = Tk()

group = LabelFrame(root,text = "最好的脚本语言是？",padx = 5,pady = 5)
group.pack(padx = 10, pady = 10)
LANGS = [('python',1),('Perl',2),('Ruby',3),('Lua',4)]

v = IntVar()

for lang,number in LANGS:
	b = Radiobutton(group,text = lang,variable = v,value=number,indicatoron = True)
	b.pack(anchor = W,fill=X)
l = Label(root,textvariable = v)
l.pack()
mainloop()
