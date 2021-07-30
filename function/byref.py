# 参照わたし（byref） <-> 値渡し（bycalue）
def add_nums(a, b):
    print(f"第一引数のaのID: {id(a)}")
    print(f"第二引数のbのID: {id(b)}")
    return a + b

one = 1
two = 2
print(f"oneのID: {id(one)}")
print(f"twoのID: {id(two)}")

# pythonはすべて参照渡し

print(add_nums(one, two))

# ただしイミュータブルなオブジェクトの場合、挙動としては値私のような渡し方
def add_one(num):
    print(f"変更前のID: {id(num)}")
    num += 1
    print(f"変更後のID: {id(num)}")
    return num

one = 1
print(id(one))
print(f"関数呼び出し前のoneのID: {id(one)}")
add_one(one)
print(f"関数呼び出し後のoneのID: {id(one)}") # 変わらない

# ミュータブルなオブジェクト
def add_fruit(fruits, fruit):
    print(f"変更前のID: {id(fruits)}")
    fruits.append(fruit)
    print(f"変更後のID: {id(fruits)}")
    return fruits

myfruits = ['apple', 'banana', 'peach']
myfruit = 'lemon'
print(f"関数呼び出し前のmyfruits: {id(myfruits)}")
add_fruit(myfruits, myfruit)
print(f"関数呼び出し前のmyfruits: {id(myfruits)}")