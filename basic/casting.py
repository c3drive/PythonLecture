# キャスティング（casting):データ型の変換
# strings
# '1'
# int
# 1
# frloat
# 1.0
# boolean
# True, False
# list
# [1, 2]
# tuple
# (1, 2)
# dictionary
# {"one": 1, "two": 2}
# set
# {1, 2}

# str(), int(), float(), list(), bool(), tuple(), set()
print(f"{type(str(1))}: {str(1)}")
print(f"{type(int('1'))}: {int('1')}")
print(f"{type(float('1'))}: {float('1')}")
print(f"{type(list('hello'))}: {list('hello')}")
print(f"{type(bool(0))}: {bool(0)}")
print(f"{type(tuple([1, 2, 2, 3, 4]))}: {tuple([1, 2, 2, 3, 4])}")
print(f"{type(set([1, 2, 2, 3, 4]))}: {set([1, 2, 2, 3, 4])}")