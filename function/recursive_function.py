# 再帰関数（recursive_function):関数内で自身の関数をcallする関数
# 階乗（factorial）：3! = 3 * 2 * 1 = 6
# n! = n * (n-1) * (n-2) * ... * 1
# n! = n * (n-1)!
# 自身の数字から-1した数の階乗をかけたものといえる

def factorial(num):
    if num == 1:
        return 1
    return num * factorial(num-1)

print(factorial(3))

# フィボナッチ数列（fibonacci）
# (0), 1, 1, 2, 3, 5, 8, 13, 21, ...
# 1つ前と２つ前の数字を足した数


# 6だったら0, 1, 1, 2, 3, 5, 8で8
# f(n) = f(n-2) + f(n-1)
def fibonacci_recursive(num):
    if num < 2:
        return num
    return fibonacci_recursive(num-1) + fibonacci_recursive(num-2)

print(fibonacci_recursive(6))

# 再起を使わないfibbonacci
def fibonacci(num):
    if num < 2:
        return num

    for i in range(num):
        if i < 2:
            two_back = 0
            one_back = 1

        else:
            two_back = one_back
            one_back = now

        now = two_back + one_back

    return now

print(fibonacci(6))

# 速度比較
for i in range(50):
    print(i, fibonacci_recursive(i)) # 遅い。もはや最後までいけない
    print(i, fibonacci(i)) # 早い。