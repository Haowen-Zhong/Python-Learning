from tkinter import *
root = Tk()
textLabel = Label(root,text = "您所下载的内容需要高等广义相对论的知识，\n您暂时无法学习",
				  justify=LEFT,
				  padx = 10,
				  pady = 10)
textLabel.pack(side = LEFT)
photo = PhotoImage(file="Figure_1.png")
imgLabel = Label(root,image=photo)
imgLabel.pack(side = RIGHT)
mainloop()

