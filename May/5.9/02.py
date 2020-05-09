#分组
#匹配数字0-100数字
import re
n = '9'
result = re.match('[1-9]?\d',n)
print(result)
n = '100'
result = re.match('[1-9]?\d',n)
print(result)
result = re.match(r'^[1-9]?\d?$|100$',n)
print(result)

#验证输入的邮箱 163 126 qq
#()可以是一个整体的
'''
小括号表示分组！！！！可以结合group(i)表示取第i组内容部分
'''
#(word|word|word) 表示可以是这三个单词中的一个 而[abc]表示可以是a可以是b可以是c
email = '912391293@qq.com'
result = re.match(r'\w{5,20}@(qq|126|163)\.(com|cn)$',email)
print(result)
#不是以4,7结尾的手机号码(11位)

phone = '13823232323'
re.match(r'1\d{9}[0-35-689]$',phone)
print(phone)

#爬虫
phone = '010-123456789'
result = re.match(r'(\d{3}|d{4})-(\d{9})$',phone)
print(result)
print(result.group())
print(result.group(1))
print(result.group(2))


msg = '<html>abc</html>'
msg1 = '<html><h1>hello</h1></html>'
result = re.match(r'<[0-9a-zA-Z]+>(.+)</[0-9a-zA-Z]+>',msg)
print(result.group(1))#因为只有1个括号！
print(result.group())

#number
result = re.match(r'<([0-9a-zA-Z])+>(.+)</[(/1)]+>$',msg)
print(result.group())
result = re.match(r'<([0-9a-zA-Z])+>(.+)</[(/1)]+>$',msg1)
print(result)
