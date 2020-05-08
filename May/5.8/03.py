#看到了175，正则表达式次数
import requests
response = requests.get('http://www.12306.cn/')
print(response.text)

'''
正则表达式:
筛子的作用，匹配
灵活但难懂
'''
# qq = input('输入qq号码')
# if len(qq)>=5 and qq[0]!= '0':
# 	print("OK，你的这号码OK👌")
# else:
# 	print("你这号码不合法啊！")

import re

msg = '娜扎热巴佟丽娅'
pattern = re.compile('佟丽娅')#这里佟丽娅就是所谓正则，并且从头开始匹配 如果头就不是了那就凉了
result = pattern.match(msg)#没有匹配就会返回None 🈳️空
print(result)

msg = '佟丽娅娜扎热巴'
pattern = re.compile('佟丽娅')
result = pattern.match(msg)#没有匹配就会返回None 🈳️空
print(result)
'''
之前只是牛刀小试，现在来真的了
使用正则re模块方法：match
我现在的一个疑问是这些操作和字符串操作相比有什么优越性呢？
'''
s = '娜扎热巴佟丽娅把戴斯'

result = re.match('佟丽娅',s)
print(result)
result = re.search('佟丽娅',s)
print(result)
print(result.span())
print(result.group())#使用group方法来提取匹配的内容部分
print(result.groups())


# a2b h6k

msg = 'abcd7wae98971xgs'
s = '哈哈5'
result = re.search('[0-9]',s)
print(result)
#result = re.search('[a-z][0-9][a-z]',msg)
#print(result.group())
#正则符号