# range(start, stop, step)
for i in range(1, 7, 1): #stepのデフォルトは1なので省略化
    print(i)

for i in range(7): #startも省略化
    print(i)

for _ in range(7): #とってきた数字を使わない場合_
    print("hello")

# FizzBuzz
for i in range(1, 51):
    if i % 15 == 0:
        print("FizzBuzz")
    elif i%3 == 0:
        print("Fizz")
    elif i%5 == 0:
        print("Buzz")
    else:
        print(i)

