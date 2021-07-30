# dictionary : キーと値の組み合わせを複数保持するデータ型
fruits_colors = {'apple': 'red', 'lemon': 'Yellow', 'grapes': 'purpls'}
print(fruits_colors['apple'])

fruits_colors['peach'] = 'pink'
print(fruits_colors)

dict_sample = {1: 'one', 'two': 2, 'three': [1, 2, 3], 'four': {'inner': 'dist'}}
print(dict_sample)
print(dict_sample['four']['inner'])

colors = {}
colors[1] = 'blue'
colors[0] = 'red'
print(colors)

# .keys() .values()
for fruit in fruits_colors.keys():
    print(fruit)

for color in fruits_colors.values():
    print(color)

# 何も指定しない
for x in fruits_colors:
    print(x)

# .items()
for fruit, color in fruits_colors.items():
    print(f"{fruit} is {color}")