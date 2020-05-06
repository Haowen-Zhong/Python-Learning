__all__ = ['add','number']
#变量
number = 100
name = 'calculation'
#函数
def add(*args):
	if len(args)>1:
		sum = 0
		for number in args:
			sum += number
		return sum
	else:
		print("至少传入2个参数...")
		return 0

def subtract(*args):
	if len(args)>1:
		m = 0
		for i in args:
			m -= i
			return m
	else:
		print("至少传入2个参数...")
		return 0

def multiply(*args):
	pass

def divide(*args):
	pass

#类
class Calculate():
	def __init__(self,number):
		self.number = number
	def test(self):
		print("正在使用calculate进行运算")

	@classmethod
	def test1(cls):
		print('----------->Calculate中类方法')
#测试函数
#__name__ 在自己的模块中叫 __main__ 在别人的模块里通过引入方式调用就是模块名了！比如这里就是calculate
def test():
	print("我是测试")
	#如果不希望进行语句的调用，就会用到__name__ = 'main'
print('__name___ --->',__name__)
if __name__ == '__main__':
	print(__name__)
	test()