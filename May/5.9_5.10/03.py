import re
msg = '<html><h1>abc</h1></html>'
#起名方式: (?P<名字>正则) (?P=名字)
result = re.match(r'<(?P<name1>\w+)><(?P<name2>\w+)>(.+)</(?P=name2)></(?P=name1)>',msg)
print(result.group(1))
'''
分组()
引用分组匹配内容
1.number \number 引用第i组的数据
2.?P<name> 找到<name>组的内容
'''
#sub ------> 替换的功能 第一个参数：正则表达式，第二个参数：新的内容 第三个参数：旧的字符串
result = re.sub(r'\d+','1000','java:100,python:100')
print(result)
#替换的内容可以是一个函数
#比如希望所有数字都加1
def func(temp):
	number = temp.group()
	number_new = int(number)+1
	return str(number_new)

result = re.sub(r'\d+',func,'java:98,python:97')
print(result)
#遇到冒号或者逗号就切一刀
result = re.split(r'[,:]','java:99,python:100')
print(result)