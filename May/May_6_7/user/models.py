class User:
	def __init__(self,username,password):
		self.username = username
		self.password = password

	def login(self,username,password):
		if username == self.username and password == self.password:
			print("登陆成功")
		else:
			print("登陆失败")
	def show(self):
		print(f"{self.username},{self.password}")

	def publish_article(self,article):
		print(f"{self.username}发表了{article.name}")