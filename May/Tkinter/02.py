import tkinter as tk

class APP:
	def __init__(self,master):
		frame = tk.Frame(master)
		#自动调整位置
		frame.pack(side = tk.LEFT,padx = 10, pady = 10)#x方向，y方向间距为均10

		self.hi_there = tk.Button(frame,text="打招呼",fg = "blue",bg = "green",command = self.say_hi())#font 颜色 蓝色的 字体是打招呼
		self.hi_there.pack()
	def say_hi(self):
		print("互联网的广大朋友们大家好，我是耘蚁🐜")

root = tk.Tk()
app = APP(root)

root.mainloop()