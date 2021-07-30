import sys


# range(10)
def myrange(stop):
    start = 0
    while start < stop:
        # この関数はgeneratorと認識され、このyieldに指定した値が返る（return）
        yield start
        start += 1


mr = myrange(10)
print(type(mr))
print(mr)
print(f"myrange is using memor size: {sys.getsizeof((myrange))}")

for i in mr:
    print(i)

# generator iterator はnext()を呼ぶことでyieldの値を返す（このとき状態を保持する）
mr2 = myrange(10)
print(next(mr2)) #0
print(next(mr2)) #1
print(next(mr2)) #2
print(next(mr2)) #3
print(next(mr2)) #4
print(next(mr2)) #5
print(next(mr2)) #6
print(next(mr2)) #7
print(next(mr2)) #8
print(next(mr2)) #9
print("end of next()")
# print(next(mr2)) #10
# print(next(mr2)) #11

print("begining of for loop")
# generatorは最後まで来ているのでエラーになる
# TypeError: 'generator' object is not callable
# for i in mr2(10):
#    print(i)

# generatorを呼ぶときはobjectではなく直接呼ぶ
for i in myrange(10):
    print(i)


# challenge
# 1回のiterationで2回回っている
def even(num):
    while num != 0:
        if num % 2 == 0:
            yield num
        num -= 1


print("=" * 30)
for i in even(10):
    print(i)

print("=" * 30)
even_gen = even(10)
print(next(even_gen)) # next()関数で回せる
print(iter(even_gen)) # iter()関数でiteratorが返る

# even()はiterator