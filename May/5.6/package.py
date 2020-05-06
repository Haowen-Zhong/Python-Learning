# 包 和 文件夹是有区别的。
# 文件夹里面一般放非py文件而包里面则放py文件。
# 比如可以放图片啊，文本啊，这些东西都放在文件夹里是比较合适的。
# 当然我们也可以让文件夹变成包，只需要加一个__init__.py
#项目->包->模块->类，函数，变量

#使用包中模块中的user类

# from user import models
#
# user = models.User("admin",123456)
# user.show()

from user.models import User
user = User("admin",123456)
user.show()

from article.models import Article

article = Article('量子力学','周世勋')
article.show()
