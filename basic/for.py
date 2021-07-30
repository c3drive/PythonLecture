# forループ
fruits = ['apple', 'peach', 'grapes', 'banana']

for fruit in fruits:
    print(f"I love {fruit}!!")

for char in "hello world":
    print(f"char: {char}")

for i in range(29):
	print(i)

for _ in range(5):
	print("Hello")
	
#iterationとiterable

# challenge2
favorit_fruits = []
normal_fruits = []

for fruit in fruits:
    choice = input(f"{fruit}は好き？ y/n")

    if choice == "y":
        favorit_fruits.append({fruit})
    else:
        normal_fruits.append(({fruit}))
print(f"favarit_fruits: {favorit_fruits}")
print(f"normal_fruits: {normal_fruits}")