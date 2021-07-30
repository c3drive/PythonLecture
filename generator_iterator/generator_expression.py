import sys

square_list = [num * num for num in range(100)]
print(square_list)
print(f"square_list is using memor size: {sys.getsizeof((square_list))}")

# こちらの方がメモリ節約
square_gen = (num * num for num in range(100))
print(next(square_gen))
print(next(square_gen))
print(f"square_gen is using memor size: {sys.getsizeof((square_gen))}")

even_square = [num * num for num in range(10) if num % 2 == 0]
print(even_square)

even_square_gen = (num * num for num in range(10) if num % 2 == 0)
for num in even_square_gen:
    print(num)
