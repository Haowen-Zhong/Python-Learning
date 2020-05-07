import sys
import numpy as np
import matplotlib
print(sys.path)#导入包的搜索顺序

print(sys.version)
print(sys.argv)#运行程序时的参数，argv是一个列表，放的默认是程序本身

import time
#1. 时间戳 从公元0000年0分0秒开始
t = time.time()
print(t)
#time.sleep(3)
t1 = time.time()
print(t1)

#将时间戳转换成人可以看懂的字符串的方式
s = time.ctime(t)
#将时间戳转换成元组的方式
p = time.localtime(t)
print('ctime',s)
print('localtime',p)

#将元组转换成时间戳
print(time.mktime(time.localtime(t)))#就是可以互相转，不过精度会变差，把秒后面的都扔掉了。

#将元组的时间转成字符串
print(time.strftime('%Y-%m-%d'))
import datetime
print(datetime.time.hour)
date = datetime.date(2020,5,7)#date 是一个类属性
print(date.day)
print(date.month)
print(datetime.date.ctime(date))
print(datetime.date.today())

timedel = datetime.timedelta(hours=2)#给一个时间差值
timedel1 = datetime.timedelta(days = 3, hours = 10)
print(timedel)

now = datetime.datetime.now()#得到当前的日期和时期
print(now)
result = now - timedel#得到变化之后的时间
print(result)
result = now + timedel#得到变化之后的时间
print(result)
result = now + timedel1#得到变化之后的时间
print(result)

