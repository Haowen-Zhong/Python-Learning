import tkinter as tk
#实例化一个程序
app = tk.Tk()
#标题栏
app.title("Haowen demo")
#显示文本
theLabel =tk.Label(app,text="我的第一个窗口程序")
#自动调节组件的尺寸和大小
theLabel.pack()
#这是进入循环由孤立程序Tkinter来接管整个程序
app.mainloop()


