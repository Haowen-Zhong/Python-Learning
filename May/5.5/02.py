#这个是要注意的。
class Person:
	def __init__(self) -> object:
		self.__money = 200
		self.name = "匿名"
	def show1(self):
		print(f'{self.name},money:{self.__money}')

class Student(Person):
	def __init__(self):
		#super().__init__() 🉑️
		#super(Student,self).__init__() 🉑️
		Person.__init__(self)
		self.__money = 500
	def show(self):
		#直接是无法继承私有属性的！
		print(f'{self.name},money:{self.__money}')


student = Student()
student.show()
student.show1()