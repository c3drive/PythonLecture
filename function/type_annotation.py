# Type annotation
# あまり指定しているプロジェクトはない。
# Pythonの動的型付け言語なので思想とも合わない
def add_nums(num1: int, num2: int) -> int:
    return num1 + num2

# Pythonは動的型付け言語 <-> 静的型付け言語
one = 1
two = 2
one = "hello"
# 使えてしまう
print(add_nums("1", "2"))