# Decorator:関数に機能を付属する（デコレートする）

def greeting(func):
    def inner(name):
        print("Hello")
        func(name)
        print("Nice to meet you")
    return inner

def say_name(name):
    print(f"I'm {name}")

# say_nameをgreetingでデコレートした状態
# f = greeting(say_name)
# f("Jiro")

# 関数名と同じ変数にするとあたらしい関数が作れる
say_name = greeting(say_name)
say_name("Jiro") # say_nameを使っているはずなのにデコレートされているものになる

def greeting2(func):
    # デコレータはどう使われるか引数の数がわからないためargs, kwargsにしておく
    def inner(*args, **kwargs):
        print("Hello")
        func(*args, **kwargs)
        print("Nice to meet you")
    return inner

# @XXX(デコレータをつける）
@greeting2
def say_name_origin(name, origin):
    print(f"I'm {name}, I'm from {origin}")

say_name_origin("Taro", "Saitama")