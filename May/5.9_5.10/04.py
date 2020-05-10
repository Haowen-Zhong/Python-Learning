import re
#默认是贪婪的，一直取到不行为止
msg = 'abc123abc'
result = re.match(r'abc(\d+)',msg)
print(result.group())
#可以通过加问好变成非贪婪！
result = re.match(r'abc(\d+?)',msg)
print(result.group())

'''
进程：
单核CPU实现多任务是串行的，看似是同时执行的，其实不是
多核CPU实现多任务：真正的并行执行多任务只能在多核CPU上实现，但是由于任务数量远远多余CPU的核心数量，操作系统也会
进行调度
并发和并行：
**并发**：当有多个线程在操作的时候，如果系统只有一个CPU则它根本不可能真正同时进行一个以上的线程，它只能把CPU运行时间
划分成若干个时间，一个运行，其他挂起。
**并行**：若系统有一个以上CPU使，线程操作可能飞并发，当一个CPU执行一个线程时，另一个CPU可以执行另一个线程，两个线程
互不抢占资源。
实现多任务方式：
多进程
多线程
协程

进程 > 线程 > 协程

进程优点：稳定性高，一个崩了，不会影响其他进程
进程缺点：开销大
'''
# 进程创建
#返回0 和 子进程PID（在父进程中）
#<0 失败
#=0 在子进程中的返回值
#>0 在父进程中的返回值
# import os
# pid = os.fork()
# if pid <0:
# 	print("糟糕")
# elif pid ==0:
# 	print("this is child process")
# else:
# 	print("this is parent process")
# print("----the end ----")
#这个可能也能用
import os
from multiprocessing import Process
from time import sleep
def task1():
	while True:
		sleep(2)
		print("这是任务1......",os.getpid(),'------',os.getppid())
def task2():
	while True:
		sleep(1)
		print("这是任务2.....",os.getpid(),'------',os.getppid())
if __name__ == '__main__':
	# 子进程
	print(os.getpid())
	p = Process(target = task1,name='任务1')
	p1 = Process(target = task2, name='任务2')
	p.start()
	p1.start()
	print(p.name)
	print(p1.name)
	print('--------------')
	print('************')
	#task1()
	#task2()


