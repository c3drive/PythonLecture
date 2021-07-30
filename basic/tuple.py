# tuple(タプル）:変更できないリスト[]ではなく()を使う
# 変更させたくないと言うよりは、変更する必要がない時タプル
date_of_birth = (1983, 6, 18)
print(date_of_birth)

# enumerateの時帰ってきたものはタプル
# for tuple in enumerate(fruits):
#    print(tuple) # (0, 'apple')

#unpack
year, month, date = date_of_birth
print(year)
print(month)
print(date)