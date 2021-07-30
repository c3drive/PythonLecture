# 変数定義
# currect
x = 1
yy = 1
# worng
x  = 1
yy = 1

# 関数の引数の「=」にはスペース不要
def complex(real, imag=0.0):
    return complex(real=1, imag=2)

#Wrong
def complex(real, imag = 0.0):
    return complex(real = 1, imag = 2)

# operatorの周りにスペース一個、operatorにpriorityがある場合はスペースをなくす
x = x + 2
x += 2
x = x*2 - (1*1) # *が先に計算されるためプライオリティがある状態

# wrong
x=x+1
x +=2
x = x * 2 - (1 * 1)

# カンマの後にはスペースを入れる、カンマの後にとじかっこがくる場合はスペース不要
# correct
range(1, 11)
a = [0, 1, 2]
foo = (0,)

# バージョン管理を意識した書き方はOK
# correct
FIELD = [
    'setup.co',
    'to.eeee',
]

# wrong
FIELD = ['setup.ee', 'dddd']

# 行の折り返し（80文字と言われているが一般的に短く、守っていないプロジェクトが多い。pyCharmもデフォルト120
foo = long_function_name(var_one, war_two,
                         var_three, var_four)

foo = long_function_name(
    var_one, war_two,
    var_three, var_four)

# wrong
foo = long_function_name(var_one, war_two,
    var_three, var_four)
    print(var_one)

# '\'で区切って改行する
print("このように表示する文章が長かったりする場合は\
バックスラッシュで区切ると改行できます")

a = 1000000000000000 \
    + 20000000000000 \
    + 33333

# wrong
a = 200000000000 + \
    300 + \
    4

# 関数間は2行開ける
def fuc1():
    pass


def func2():
    pass

# Classのmethodは1行
class MyClass:
    def __init__(self):
        pass

    def method(self):
        pass

# importのStyle
# correct
import os
import sys
from subprocess import Popen, PIPE

# wrond
import os, sys

# 順番
# 1.Standard Library(time, sys)
# 2.Third party(numpy, pandas)
# 3.Our Library
# 4.Local Library
# それぞれ1行開ける（abc順）

# なるべくrelative importではなくabsolute importにする
import mypakc.sibling
from mypakg.sibling
from mupakg import sibling
from mypkg.sibling import example

# 長い場合は、relative importでもOK
from package.subpackage1.subpackage2.subpackage3.subpackage4.module import function

# コメント
# ・コメントは常に最新にする。コメントとコードの中身が異なるなら、コメントはない方がマシ
# ・なるべく英語で書く。絶対に日本語がわからない人が読まないなら日本語でもOK
# ・書くときは文章で格納が望ましい
# ・#のあとは半角スペースを入れる
# ・インラインコメントはコードの後に半角スペースを2つ入れて#を書く
# ・Docstringは基本的に全てのmodule, function, class, methodにつける（non publicな外からアクセスしない関数には不要）
# ・そのコートが「何をしているか」より「何故そう書いたのか」の方が有益

# wrong
# 残高が引き落とし額より大きければXX
if balance > withdraw
    pass

# correct
# 残高が足りない場合を考慮する
if balance > withdraw
    pass

# 命名規則（naming conbention）
# 変数名は関数（メソッド）名：snake_case 例）balance, image_height
# クラス名：CamelCase 例）Person, MyClass
# モジュールやパッケージ名：なるべく短いLower caseで、必要であればsnake_case 例）time, numpy

# アンダースコア
# - _xxx: internal use only(non publuc)の意味
# - xxx_: Pythonですでにつかwらえている単語を使いたいとき　例）type_
# - __xxx: クラスの属性として使うことで名前就職される
# - __xx__: magic methodと呼ばれるもので、Pythong後口説に設定しているもの。開発者が定義することはない（overrideすることはある）
# - _: 最近実行した戻り値や、iteration時に使わない関数

for _ in range(20):
    pass

# l, I, O 一文字の変数は1や0に見間違えるので使わない
# correct
lenght = len(letter)

# wrong
l = len(letter)

# Constants（先言語変更しない変数）は大文字のsnakecaseを使う
PI = 3.14

# Return(意味がなくても全部書く）
def foo(x):
    if x >= 0:
        return math.sqrt(x)
    else:
        return None

# オブジェクトタイプの確認はisinstance()を使う
# correct
if isinstance(obj, int)
# wrong
if type(obj) is type(1)

# Booleanに比較演算子を使わない
bool_var = True

# correct
if bool_bar:
    pass

# wrong
if bool_var == True:
    pass

# type hint(type annotation)
# 1つでもhintを付けたら全てにつける
# Pythonがtypeのチェックをしてくれるわけではない
# Pythonは同的片付け言語であることを意識
# type hintを矯正したり、命名規則に入れるべきではありません
def greeting(name: str) -> str:
    return "Hello" + name

# wrong
def greeting(name:str):
    reteurn "Hello" + name