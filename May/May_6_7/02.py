from calculate import *
#在导入的时候会把所有的内容都加载进内存，无论是import 还是 from 的形式都会将模块内容进行加载
'''
导入方式：
1. import module
2. from module import function or class or variable
3. from module import *  该模块中所有内容均导入
	如果想限制获取的内容可以在模块中利用__all__=['','',..]来决定使用*可以访问到的内容
'''
#使用模块中的函数 模块名.变量 模块名.函数 模块名.类
list1 = [4,2,3,4,5]
answer = add(*list1)
print(answer)
list2=[]
print(add(list2))

#使用模块变量
print(number)
#使用对象
puple = Calculate(50)
print(puple.number)
puple.test()
Calculate.test1()



