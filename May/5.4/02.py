#Student Book Computer


class Book:
	def __init__(self,bname,author,number):
		self.bname = bname
		self.author = author
		self.number = number
	def __str__(self):
		return self.bname +'---'+self.author+'---'+str(self.number)

class Computer:
	def __init__(self,brand,type,color):
		self.brand = brand
		self.type = type
		self.color = color
	def online(self):
		print("正在使用电脑上网...")
	def __str__(self):
		return self.brand+'----'+self.type+'----'+self.color

class Student:
	def __init__(self,name,book,computer):
		self.name = name
		self.book = []
		self.book.append(book)
		self.computer = computer

	def borrow_book(self,book):
		for borrow_book in self.book:
			if borrow_book.bname == book.bname:
				print("您已经借过这本书了")
				break
		else:
			#将这本书添加到列表中
			self.book.append(book)
			print("添加成功")

	def show_book(self):
		for book in self.book:#book 是Book对象
			print(book.bname)
	def __str__(self):
		#return self.name+'---'+self.computer+'---'+self.book
		#return self.name+self.computer+self.book 这是不行的，因为computer是一个类型，不是字符串！
		return self.name+'----'+str(self.computer)+str(self.book)

computer = Computer('Mac','Mac Pro 2020','深灰色')
book = Book('盗墓笔记','南派三叔',10)
student = Student('浩文哥',book,computer)
print(student)
#先看看我借了什么书
student.show_book()
book1 = Book('鬼吹灯','天下霸唱',8)
student.borrow_book(book1)
print('--------------')
student.show_book()
book2 = Book('盗墓笔记','南派三叔',10)
student.borrow_book(book2)
print('--------------')
student.show_book()
