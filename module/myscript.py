# 標準ライブラリ、サードパーティのライブラリ、自分たちのライブラリ、ローカルのライブラリ
# a-z順などがわかりやすい
import sys
# module全部
# import mymodule
# mymodule.myfunc()
# print(mymodule.myvariable)

# 別名。自前で作ったパッケージ名につけること非推奨
import mymodule as mm
mm.myfunc()
print(mm.myvariable)
mm._anotherfunc()

# 部分的にimport
# from mymodule import myfunc, myvariable, _anotherfunc
# myfunc()
# print(myvariable)
# _anotherfunc()

# 非推奨だが以下で全ての関数が使える。ただし_はimportされない
# from mymodule import *
# myfunc()
# print(myvariable)

# Pythonはimportにてビルトイン、なければsys.pathを見る
# ＝ビルトインではないかつ、sys.pathにないモジュールはimportできない
print(sys.path)

# 何もしないとsys.pathにはないモジュールを呼ぶ場合
sys.path.append("/Users/yukokanai/work/python/PythonLecture/function/")
import docstring

print(docstring.multiply(3, 4))