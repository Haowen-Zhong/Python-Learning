from tkinter import  *

root = Tk()

v = IntVar()

Radiobutton(root,text='One',variable = v, value = 1).pack(anchor = W)
Radiobutton(root,text='Two',variable = v, value = 2).pack(anchor = W)
Radiobutton(root,text='THREE',variable = v, value = 3).pack(anchor = W)
Radiobutton(root,text='FOUR',variable = v, value = 4).pack(anchor = W)
l = Label(root,textvariable = v)
l.pack()
mainloop()