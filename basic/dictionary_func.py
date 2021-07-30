fruits_colors = {'apple': 'red', 'lemon': 'Yellow', 'grapes': 'purpls'}

# print(fruits_colors['peach'])はエラー

if 'peach' in fruits_colors:
    print(fruits_colors['peach'])
else:
    print('the key is not found')

# .get()
# キーがない場合のデフォルトの値を返すことができる
fruit = input("フルーツの名前を指定してください")
print(fruits_colors.get(fruit, 'Nothing'))

# .update()
# deictionary同士の結合
fruits_colors2 = {'peach': 'pink', 'kiwi': 'green'}
fruits_colors.update(fruits_colors2)
print(fruits_colors)

