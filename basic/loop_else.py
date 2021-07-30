# while else
fruits = ['apple', 'peach', 'grapes', 'banana']

for fruit in fruits:
    choice = input(f"あなたが探しているフルーツは{fruit}ですか？ y/n")
    if choice == "y":
        print("見つかってよかったですね")
        break
    else:
        print("そうですか")
else:
    print("お探しのフルーツは見つかりませんでした")

count = 0
while count < 10:
    print(count)
    count += 1
else:
    print("countは10未満ではなくなりました")