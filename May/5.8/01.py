import random
ran = random.random()#0~1随机小数
print(ran)
list = []
for i in range(20):
	ran = random.randrange(1,10,2)#可以出现1~10 步长为2的数
	list.append(ran)
list = set(list)
print(list)
ran = random.randint(1,10)
print(ran)
#随机选取一个倒霉蛋
list1 = ['盈盈','浩文','阿鹏','阿文','倒霉蛋😓']
ran = random.choice(list1)
print(ran)
#洗牌
card = ['红桃A♥️','♣梅花8','方片♦️K','♠️黑桃J']
random.shuffle(card)
print(card)
#验证码，大小写字母与数字的组合
def func():
	code = ''
	for i in range(4):
		ran1 = str(random.randint(0,9))
		ran2 = chr(random.randint(65,90))#转换成ASCII码对应的东西
		ran3 = chr(random.randint(97,122))

		code += random.choice([ran1,ran2,ran3])
	return code

print(func())

