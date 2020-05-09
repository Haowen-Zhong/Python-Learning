import re
#[]表示一个范围，其中装要匹配的东西
msg = 'abcd7wae98971xgs'
s = '哈哈5'
result = re.search('[0-9]',s)
print(result)
s = '3y2u'
result = re.search('[0-9][a-z]',s)
print(result)
s = '3y2u'
result = re.search('[a-z][0-9][a-z]',s)
print(result)
#Note:Search找到一个就不找了，非常偷懒。
#下面介绍findall函数，他很好，可以找到全部。
#匹配整个字符串
s = '2u3y8i99a'
result = re.findall('[a-z][0-9]',s)
print(result)
#不过他还是不够聪明
s = 'abcde'
result = re.findall('[a-z][a-z]',s)
print(result)

#a7a a88a a78a
#只要字符串前后是字母，中间是数字就符合要求
'''
我发现它解决不了共用的问题。
这下就需要新的工具了：
*:用于将前面的模式匹配0次或多次	>=0
+：用于将前面的模式匹配1次或多次  >=1
？：用于将前面的模式匹配0次或1次 <=1
{m}用于验证将前面的模式匹配m次
{m,n}用于验证前面的模式匹配m-n次
也可以写成{m,}{,n}用来表示你懂的
^ 默认从头比较
$ 匹配到结尾处
'''
msg = 'a77778ab89bsdw8u98977a'
result = re.findall('[a-z][0-9]+[a-z]',msg)
print(result)

'''
eg.QQ号码验证5-11位的数字，而且0不能作为开头
'''
qq = '253534809'
result = re.match('^[1-9][0-9]{4,10}$',qq)
print(result.group())
qq = '253534801231231231239'
result = re.match('^[1-9][0-9]{4,10}$',qq)
print(result)
result = re.match('^[1-9][0-9]{4,}$',qq)
print(result.group())
print(result)
qq = '253534809'
result = re.match('^[1-9][0-9]{,10}$',qq)
print(result.group())

'''
用户名可以是字母或者数字，不能是字母开头，用户名必须六位以上
'''

username = '001admin'
#必须匹配到结尾，不然你有一段满足就直接觉得你满足了，这是不行的！
result = re.match('^[a-zA-Z][0-9a-zA-Z]{5,}$',username)
print(result)
username = 'admin518'
result = re.match('^[a-zA-Z][0-9a-zA-Z_]{5,}$',username)
print(result)
'''
\A:表示从字符串开始处匹配
\Z:表示从结束出匹配，如果存在换行，只匹配到换行前的结束字符串
\b:表示匹配一个单词边界，就是单词和空格间的位置
\B:匹配非单词边界
\d :匹配任意数字
\D：匹配任意非数字[^\D]写括号里的^表示非
\s:表示任意空白字符
\S:表示任意非空白字符
\w:匹配任意字符和数字以及下划线等价于[0-9a-zA-Z_]
\W:匹配任意非数字字母以及下划线
.：用于匹配除了换行符之外的所有字符
'''
username = 'admin518'
result = re.match('^[a-zA-Z]\w{5,}$',username)
print(result)

#希望找到所有的py文件
msg = 'aa.py ab.txt bb.py kk.png jj.tex apyb.txt'
result = re.findall('py\\b',msg)#这里不能只用\b因为\b是有转义字符的。所有可以\\或者r
print(result)
result = re.findall(r'py\b',msg)
print(result)
result = re.findall(r'\w*\.py\b',msg)
print(result)

phone_number = '13567238791'
result = re.match('^1[35678]\d{9}$',phone_number)
print(result.group())




