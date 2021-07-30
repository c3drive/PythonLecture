fruits = ['apple', 'lemon', 'peach']

# iteratorは、next()関数で回すことができ、iter()関数でiteratorを返すものの総称
# 以下は回せないのでiteratorではない
# print(next(fruits))

# iter()関数で、iteratorを返すものをiterableという
# listはiteratorではないがiterable
fruits_iterator = iter(fruits)
print(next(fruits_iterator))

# iter関数を使っても自分自身を返している（idが一緒）
print(id(fruits_iterator))
print(id(iter(fruits_iterator)))

print("=" * 30)
print(next(fruits_iterator))
print(fruits_iterator.__next__())
