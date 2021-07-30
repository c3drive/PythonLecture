# input():　ユーザの入力した値（文字列）を取得する

# age = input("何歳ですか？")
# print(f"あなたは{age}歳です")

# intを使いたい場合
age = int(input("何歳ですか？"))
game_text = """プレイするゲームを選択してください
1:ルーレット
2:ブラックジャック
3:ポーカー
"""

if age >= 18:
    print("どうぞお入りください")

    game = input(game_text)
    if game == '1':
        print("あなたはルーレットを選びました")
    elif game == '2':
        print("あなたはブラックジャックを選びました")
    elif game == '3':
        print("あなたはポーカーを選びました")
    else:
        print("1~3を選んでください")
else:
    print("18歳未満の方はカジノへ入れません")