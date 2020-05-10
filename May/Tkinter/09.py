from tkinter import *

root = Tk()
LANGS = [('python',1),('Perl',2),('Ruby',3),('Lua',4)]
v = IntVar()
v.set(1)

for lang,number in LANGS:
	b = Radiobutton(root,text = lang,variable = v,value=number,indicatoron = False)
	b.pack(fill = X)
l = Label(root,textvariable = v)
l.pack()
mainloop()
