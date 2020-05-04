#在Python2中才有区别
#经典类
class P1:
	def foo(self):
		print('p1-->foo')
	def bar(self):
		print('p1-->bar')
class P2:
	def foo(self):
		print('p2-->foo')
class C1(P1,P2):
	pass

class C2(P1,P2):
	def bar(self):
		print('C2-->bar')

class D(C1,C2):
	pass
d = D()
print(D.__mro__)
#从左到右，从下到上
#这是广度优先

#新式类
class P1(object):
	def foo(self):
		print('p1-->foo')
	def bar(self):
		print('p1-->bar')
class P2(object):
	def foo(self):
		print('p2-->foo')
class C1(P1,P2):
	pass

class C2(P1,P2):
	def bar(self):
		print('C2-->bar')

class D(C1,C2):
	pass
d = D()
d.bar()
d.foo()
print(D.__mro__)
#这是广度优先

