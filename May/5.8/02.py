#chr ord

print(chr(65))
print(ord('A'))#转换成对应的unicode码
print(ord('上'))
print(ord('下'))
print(chr(19979))
print(chr(35562))#属实牛逼

#hushlib
#加密算法：md5 sha1 sha256是不可逆的
#base64是可逆的
import hashlib
#按算法加密是固定的🧷🔐，同样的东西加密都是一样的
msg = '于鹏中午一起吃饭去！'
md5 = hashlib.md5(msg.encode('utf-8'))#加密
print(md5)
print(md5.hexdigest(),'len=',len(md5.hexdigest()))
sha1 = hashlib.sha1(msg.encode('utf-8'))
print(sha1.hexdigest(),'len=',len(sha1.hexdigest()))
sha256 = hashlib.sha256(msg.encode('utf-8'))
print(sha256.hexdigest(),'len=',len(sha256.hexdigest()))

password = '123456'
list1 = []
sha256 = hashlib.sha256(password.encode('utf-8'))
list1.append(sha256.hexdigest())

pwd = input("输入密码")
sha256 = hashlib.sha256(pwd.encode('utf-8'))
pwd = sha256.hexdigest()
print(pwd)
print(list1)
for i in list1:
	if pwd == i:
		print("登陆成功")




