# リスト(lists)：複数のオブジェクトを順序づけて保存するデータ型
# []で括って、,（カンマ）で各オブジェクトを区切る

fruits = ['apple', 'peach', 'melon', 'grapes']

hetro_list = ['string', 1, 3.4, True, fruits]

print(hetro_list)
print(fruits[0])
print(fruits[-3])
print(hetro_list[-1][-1])

# .append: 新しいオブジェクトを追加する
# .insert: 指定したindexに指定したオブジェクトを追加する
# .remove: マッチした最初のオブジェクトを除く
# .sort:　昇順にする
# len(): リストの要素数を取得する

fruits.append('banana')
print(fruits)

fruits.insert(3, 'lemon')
print(fruits)

fruits.remove('peach')
print(fruits)

fruits.sort()
print(fruits)

fruits.sort(reverse=True)
print(fruits)

print(len(fruits))

print(len("hello"))