#这是不可以的哦！直接会覆盖，不存在重载
# class Person:
# 	def __init__(self,name):
# 		self.name = name
# 	def eat(self):
# 		print("-------------->eat")
# 	def eat(self,food):
# 		print('-------------->eat',food)
# p = Person('jack')
# p.eat()
class A:
	def test(self):
		print('------->AAAAAAAAA')
class B:
	def test1(self):
		print("--------->BBBBBBBBB")
	def test(self):
		print("--------->BBBBBBBBB")
class C(A,B):#2个父类
	def test2(self):
		print('---------->CCCCCCCC')

	def test(self):
		print('---------->CCCCCCCC')
c = C()
c.test()
c.test1()
c.test2()

class Base:
	def test(self):
		print('-----Base-----')
class A(Base):
	def test(self):
		print("--->AAAAA")
class B(Base):
	def test(self):
		print("----->BBBBB")
class C(Base):
	def test(self):
		print("----->CCCCC")
class D(A,B,C):
	pass
d = D()
d.test()#调用第一个父亲👨的。
import inspect
print(inspect.getmro(D))#搜索的顺序！D-->A-->B-->C-->Base-->object
print(D.__mro__)
'''
Python允许多继承，遵从广度优先准则。
class 子类(父类1，父类2...):
	pass
如果父类中存在相同方法名的方法，搜索的顺序是根据广度优先准则的。
'''