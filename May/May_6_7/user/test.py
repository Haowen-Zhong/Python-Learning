#都是从项目最外层开始的！
from May_6_7.user.models import User
from May_6_7.article.models import *
#from .models import User # 这是从当前目录下导入models
from May_6_7.calculate import add
user = User("周世勋","123456")
user.login("周世勋","123456")
article = Article("量子力学","周世勋")
user.publish_article(article)

list1 = [12,3,4,5,209]
print(add(*list1))