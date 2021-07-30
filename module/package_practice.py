# 一番安全なimport
import myfirstpackage.module1
# import myfirstpackage.subdir.module2

myfirstpackage.module1.myfunc()

# from myfirstpackage.subdir.module2 import *
# と__init__.pyに定義することで、subdirはmyfirstpackageのpackageのように読み込める
myfirstpackage.myfunc()

from myfirstpackage import module1
from myfirstpackage.subdir import module2

myfirstpackage.subdir.myfunc2()

module1.myfunc()
module2.myfunc()

# 名前がかぶる。
from myfirstpackage.subdir.module2 import myfunc
myfunc()
