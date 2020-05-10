from tkinter import *
root = Tk()
photo = PhotoImage(file = "Figure_1.png")
theLabel = Label(root,
				 text = "学Python\n到FishC",
				 justify = LEFT,#字符串左对齐
				 image = photo,
				 compound = CENTER,
				 font = ("宋体",20),
				 fg = "white",
				)
theLabel.pack()
mainloop()
