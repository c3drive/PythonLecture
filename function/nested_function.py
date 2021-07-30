# 関数の中で関数を定義（nested_function）
msg = "I am global"

def outer(outer_param):
    msg = "I am outer"

    def inner():
        inner_variable = "inner var"
        nonlocal msg # outer functionの変数であることを明示
        msg = "I am inner function"
        print("This is inner function")
        print(outer_param)
        print(msg)
    inner()
#    print(inner_variable)
    print(msg)

outer("outer_arg")
# inner() # 外からは呼べない
print(msg)