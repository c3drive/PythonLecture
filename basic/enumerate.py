
fruits = ['apple', 'peach', 'grapes', 'banana']

for idx, fruit in enumerate(fruits):
    print(idx)
    print(fruit)

# enumerateがないを返すか
for tuple in enumerate(fruits):
    print(tuple) # (0, 'apple')