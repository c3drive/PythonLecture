age = int(input("何歳ですか？"))

game_dict = {'1': 'ルーレット', '2': 'ブラックジャック', '3': 'ポーカー'}

if age >= 18:
    print("どうぞお入りください")

    while True:
        print("プレイするゲームを選択してください")
        for num, game_name in game_dict.items():
            print(f"{num}: {game_name}")
        game = input(":")
        if game in game_dict:
            print(f"あなたは{game_dict[game]}を選びました")
            break
        else:
            print("正しい選択を選んでください")
else:
    print("18歳未満の方はカジノへ入れません")