def func(first, second="two", third="three"):
    print(f"first: {first}, second: {second}, third: {third}")

# argument <-> parameter
func("1", "2", "3")

# 順番が違っても名前を優先
func("1", third="3", second="2")

# 指定しない場合キーワードパラメータ（デフォルト）
func("1","3")