def split_bill(price):
    num = input("何人で割り勘しますか？")
    try:
        each = price / int(num)
        return "try" # elseが実行されない（finallyはされる）
    except ZeroDivisionError as e:
        print("0で割ることはできません。正しい値を入力してください。")
        print(e)
    except ValueError as e:
        print("数字を入力してください。")
        print(e)
    else:
        # print(0 / 0)
        print(f"一人{each}円です。")
    finally:
        print("ご利用ありがとうございます。")
        return "finally" # tryの中の物は実行されない


if __name__ == "__main__":
    print(split_bill(100000))