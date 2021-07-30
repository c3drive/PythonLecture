# [:]を使って、複数の要素を取ってくることができる（slicing）
even = [2, 4, 6, 8, 10, 12]

# 基本は[開始:未満]
print(even[1:4])
print(even[:4]) # 0は省略可能

print(even[3:5])
print(even[3:-1])

print(even[3:]) # 最後まで
print(even[:]) # すべて
text = "hello world" # 文字列
print(text[3:])

# [開始:未満:step]
count = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
print(count[2:10:2])

print(count[::-1]) # 全部撮ってきて逆順