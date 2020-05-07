'''
这是错误的方式！！！！我们要避免这种事情！大型的Python项目中需要很多模块，由于架构不当
可能会出现模块之间的相互导入。
循环导入：在A里导入B，在B里导入A
A模块:
	def test():
		f()
B模块:
	def f():
		test()
避免产生循环导入的解决方式：
	1.重新架构
	2.改变导入的位置
	3.把导入语句放到模块的最后。
	总之具体问题具体分析
'''
from May_6_7.cyclic_import_2 import func
def task1():
	print("------------task1")
def task2():
	print("------------taks2")
	func()

if __name__ == '__main__':#这个很重要！因为防止在别人调用的时候把这些都跑一遍。
	task1()
	task2()