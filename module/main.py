import mymodule

mymodule.myfunc()
print(__name__)
# This is a sample Python script.

# Press <no shortcut> to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# __name__は実行されたモジュールが自分の場合"__main__"となる
# importdで呼ばれた場合は、モジュール名
# 以下のようにすることで、importの読み込み時に実行されなくなる
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
