#封装 继承 多态--->面向对象

'''
Pet 父类 Cat Dog 子类
Pet 大类型 Cat Dog 小类型
'''



class Person:
	def __init__(self,name):
		self.name = name
	def feed_pet(self,pet):#pet既可以接收cat，也可以dog，也可以tiger。这不是严格的多态，其他语言严格只接收Pet子类
		#那我们就可以通过利用isinstance来判断对象的类！
		if isinstance(pet,Pet):#判断是否是子类。
			print(f"{self.name}喜欢养宠物：{pet.role},昵称为:{pet.nickname}")
		else:
			print("不是宠物！不能养！")
			if isinstance(pet,Tiger):
				print("你这是大老虎🐯！！你会被吃掉哒～")

class Pet:
	role = 'Pet'
	def __init__(self,nickname,age):
		self.nickname = nickname
		self.age = age
	def show(self):
		print(f'昵称:{self.nickname},年龄：{self.age}')
class Tiger:
	def eat(self):
		print("???!🐯！！")
class Cat(Pet):
	role = '🐱'
	def catch_mouse(self):
		print("抓老鼠🐭")

class Dog(Pet):
	role = '🐶'
	def watch_house(self):
		print("看家高手👀🏠")

#创建对象
cat = Cat("租租",21)
dog = Dog('沫沫',21)
tiger = Tiger()
person = Person('盈盈')

person.feed_pet(cat)
person.feed_pet(tiger)
