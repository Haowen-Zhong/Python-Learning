'''
一个题目
公路（Road）
属性：公路名称，公路长度
车（Car）
	属性：车名，时速
方法:
	1.求车名在那条公路上以多少的时速行驶了多长
		get_time(self,road)
	2.初始化车属性信息__init__方法
	3.打印对象显示车的属性信息
'''
import random

class Road:
	def __init__(self,name,len):
		self.name = name
		self.len = len

class Car:
	def __init__(self,brand,speed):
		self.brand = brand
		self.speed = speed
	def get_time(self,road):
		ran_time = random.randint(1,10)
		msg = f"{self.brand}的车在{road.name}上以{self.speed}的速度行驶了{ran_time}小时"
		print(msg)
	def __str__(self):
		return f"{self.brand}的车，速度{self.speed}"
	def __call__(self):
		return f"{self.brand}的车，速度{self.speed}"
#这里只是用到了把对象传给方法，其实本质上还是一样，把类对象看成我们自定义的变量，把这个变量传给一个函数是很自然的事情
avenue = Road("京藏高速",1000)
bench = Car("benz",200)
bench.get_time(avenue)
print(bench)
print(bench())
avenue.name = "京哈高速"
bench.get_time(avenue)