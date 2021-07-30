# *args
# print("hello", "world", "test")
def get_average(*args):
    print(*args)
    print(args)

    num = len(args)
    if num == 0:
        return 0
    total = sum(args)
    return total / num

average = get_average(1, 2, 3, 4, 5, 6, 7, 8)
print(average)

# **kwargs(*argsのディクショナリーバージョン）
def kwargs_func(**kwargs):
    print(kwargs)

    # .get(key, default)
    param1 = kwargs.get('param1', 1)
    param2 = kwargs.get('param2', 2)
    param3 = kwargs.get('param3', 3)
    print(f"parma1: {param1}, param2: {param2}, param3: {param3}")

kwargs_func(param1=10, param2=6, param3=100, param4=4)

# *と**とは、unpackin operator
numbers = (1, 2, 3)
print(*numbers)
print(1, 2, 3)

a = {'a': 1, 'b': 2}
b = {'c': 3, 'd': 4}
c = {**a, **b}
print(c)