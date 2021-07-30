import traceback


def split_bill(price):
    num = input("割り勘する人数を入力してください")
    try:
        each = price / int(num)
    except ZeroDivisionError:
        print("0で割ることはできません。正しい値を入力してください。")
    else:
        print(f"一人{each}円です。")


def check(bil):
    total_bill = sum(bil.values())
    try:
        split_bill(total_bill)
    except ValueError:
        # printだけだと隠蔽されてしまうためtracebackを使う
        # ただし、リリース時はコメントアウトする
        traceback.print_exc()
        print("エラーが出ました。やり直してください。")


if __name__ == "__main__":
    bill = {'burger': 500, 'pasta': 1400, 'fries': 300, 'egg': 200}
    check(bill)
    print("プログラムは実行されました。")
