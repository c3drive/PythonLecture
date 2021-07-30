# whileループ
count = 0
while count < 10:
    print(count)
    count += 1

# break と continue
while True:
    age = int(input("あなたは何歳ですか？"))
    if not 0 <= age < 120:
        print("入力された値は正しくありません")
        continue
    else:
        print(f"あなたは{age}歳です")
        break

# inputの時のゲームをrefactoringする
age = int(input("何歳ですか？"))
game_text = """プレイするゲームを選択してください
1:ルーレット
2:ブラックジャック
3:ポーカー
"""
if age >= 18:
    print("どうぞお入りください")

    while True:
        game = input(game_text)
        if game == '1':
            print("あなたはルーレットを選びました")
        elif game == '2':
            print("あなたはブラックジャックを選びました")
        elif game == '3':
            print("あなたはポーカーを選びました")
        else:
            print("1~3を選んでください")
            continue
        break
else:
    print("18歳未満の方はカジノへ入れません")