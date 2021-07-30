# assert
a = 1
b = 1

# a + b == 2
print(( a + b) == 2)
assert a + b == 2, "a + b is equal to 2"


def power(base, exp):
    return base ** exp


# 実際の開発ではテストはまとめてテストスクリプトで書く
assert power(3, 2) == 9, "3 ** 2 must be 9"