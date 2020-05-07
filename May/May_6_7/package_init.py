#只要你导入这个包，他就会默认调用__init__文件
#文件里的所有东西都默认直接加载到内存！
#导包就给你东西


# from May_6_7 import user
# user.create_app()
# user.test()

#from module import *是对于模块的
#from package import * 需要结合__all__
from May_6_7.user import models
#这么写只能用在__all__里出现过的东西，这个和module的用法是相反的。
from May_6_7.user import *
models.User("格里菲斯","123")
print(test.list1)