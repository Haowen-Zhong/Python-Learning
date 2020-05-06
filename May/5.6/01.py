#单例模式
#开发模式：单例模式       单个对象
# class Student:
# 	pass
#
# #创建一个对象就产生一个地址，只要不结束程序就不会收回空间
# #单例模式就是只用一个实例。
# s = Student()
# s1 = Student()
# print(s)
# print(s1)

class Singleton:
	# 私有化 单例的地址就存在__instance 里面，并且通过私有化保证外面不能乱改。
	__instance = None
	name = 'Jack'
	# 重写父类__new__
	def __new__(cls):
		print("------>__new")
		if  cls.__instance is None:
			#打完1后利用new给了我一块空间并且把这个开辟的地址给了__instance,并return出去
			#当又一次尝试创建一个实例的时候，__instance已经不是空值了，因此就走了else并且把老的地址给了他！
			cls.__instance = object.__new__(cls)
			print(cls.__instance)
		return cls.__instance
	def show(self,n):
		print('------>show',Singleton.name,n)
s = Singleton()
s1 = Singleton()
#print(s)
#print(s1)
#print(dir(Singleton))
print(s.show(5))
print(s1.show(5))
