call_count = 0

# 書き換えられたくない場合（constant cariable）
# ただし、暗黙のルールでしかなく、書き換えられる
CALL_COUNT = 0

def print_count1():
    global call_count
    global CALL_COUNT
    call_count += 1
    CALL_COUNT += 1
    print(f"関数1： {call_count}回目")
    print(f"関数1： {CALL_COUNT}回目")

def print_count2():
    global call_count
    call_count += 1
    print(f"関数2： {call_count}回目")

print_count1()
print_count2()
print_count1()
print_count2()