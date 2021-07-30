# lambda関数（無名関数）

def square(x):
    return x * x

print(square(3))

# これをlambda関数にすると
# defをとる、関数名もとる、カッコもとる
# returnもとる
# lambdaを頭につける
s = lambda x: x * x

print(s(5))

# ただしあまりこういう使い方はしない

# よく使うやり方
# 例えば以下はinner関数が簡単なのでlambda関数化できる
#def power(exponent):
#   def inner_power(base):
#      return base ** exponent
#   return inner_power

def power(exponent):
    return lambda base: base ** exponent

third_power = power(3)
print(third_power(2))

numbers = [6, 2, 5, 43, 5 , 36, 67, 2]

# 奇数だけを返す関数を作る
def filter_func(num):
    if num % 2 == 0:
        return False
    else:
        return True

# もっと簡単に
def filter_func2(num):
    return num % 2

# filterはその関数のTrueだけを返す
filtered_num = filter(filter_func, numbers)
print(list(filtered_num))
filtered_num2 = filter(filter_func2, numbers)
print(list(filtered_num2))

# filterにはlambda関数を入れることもできる
filtered_num3 = filter(lambda num: num % 2, numbers)
print(list(filtered_num3))