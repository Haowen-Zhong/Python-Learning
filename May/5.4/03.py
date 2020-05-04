#is a base class 父类/基类
#如果这么去写太冗余了
# class Student:
# 	def __init__(self,name,age):
# 		self.name = name
# 		self.age = age
# 	def eat(self):
# 		print(f"{self.name}正在吃饭")
# class Employee:
# 	def __init__(self, name, age):
# 		self.name = name
# 		self.age = age
# 	def eat(self):
# 		print(f"{self.name}正在吃饭")
# class Doctor:
# 	def __init__(self, name, age):
# 		self.name = name
# 		self.age = age
# 	def eat(self):
# 		print(f"{self.name}正在吃饭")
'''
继承：
	Student, Employee, Doctor--->都属于人类并且有大部分相同的代码，我们认为这样代码是非常冗余的，代码的可读性就不高。
	因此将相同的代码进行提取，提取到Person这个类里面。
	class Student(Person):
		pass
  	1.如果类里面不定义__init__，就直接自动调用父类的__init__
  	2.如果类继承父类也需要定义自己的__init__,就需要在当前类的__init__调用一下父类的利用super().__init__
  	3.如果父类和子类定义了相同的Method，搜索的原则是先找当前类，再找父类。
  	  这就是重写/覆盖 overwrite
'''
class Person:
	def __init__(self, name, age):
		self.name = name
		self.age = age
	def eat(self):
		print(f"{self.name}正在吃饭")
	def run(self):
		print(f"{self.name}正在跑步")

#开始继承，会把父类里面的所有东西都继承！所有！所有！！
class Student(Person):
	def __init__(self,name,age,clazz):
		super(Student,self).__init__(name,age)#表示调用父类的动作 #super()！！！
		self.clazz = clazz
	def study(self,course):
		print(f"{self.name}正在学习{course}")
	def eat(self,food):
		print(f"{self.name}正在吃饭,{self.name}最喜欢吃：{food}")
class Doctor(Person):
	def __init__(self,name,age,patient):
		super(Doctor,self).__init__(name,age)
		self.patient = patient
class Employee(Person):
	def __init__(self,name,age,salary,manager):
		super(Employee,self).__init__(name,age)
		self.salary = salary
		self.manager = manager


Yingying = Student("盈盈",20,"物理1702")
Yingying.run()
Yingying.study("量子电动力学QED")
Yingying.eat("狮子头盖饭")
Yingying.eat("满汉全席")
print(Yingying.age)
Qianqian = Doctor('钱钱',21,"🐷")
print(Qianqian.patient)
Qianqian.run()
zhuzhu = Employee('猪猪',21,100000,'king')
zhuzhu.eat()
