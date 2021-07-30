import re

# Regular Expression（正規表現　通称RegEx）

email = "myemail@gmail.com"
print("@" in email)
matshed = re.search('@\w+\.', email)
print(matshed)

# metacharacter
# []
print(re.search('[abc]', 'cseaweta1'))
print(re.search('[a-c]', 'cseaweta1'))
print(re.search('[0-9]', 'cseaweta1'))

# ^ 最初の文字
print(re.search('^[abc]', 'cseaweta1'))

# {n} n回リピート
print(re.search('^[0-9]{4}', '2021/03/31'))
print(re.search('^[0-9]{4}', '21/03/31'))

# {n,m} 最低n回、最高m回リピート
print(re.search('^[0-9]{2,4}', '2021/03/31'))
print(re.search('^[0-9]{2,4}', '21/03/31'))

# $ 最後の文字
print(re.search('[0-9]{2}$', '2021/03/31'))
print(re.search('[0-9]{2}$', '21/03/1'))

# * 左のパターンを0回以上繰り返す
print(re.search('a*b', 'a'))
print(re.search('a*b', 'b'))
print(re.search('a*b', 'ab'))

# + 左のパターンを1回以上繰り返す
print(re.search('a+b', 'a'))
print(re.search('a+b', 'b'))
print(re.search('a+b', 'ab'))

# ? 左のパターンを0回か1回繰り返す
print(re.search('ab?c', 'abbbc'))
print(re.search('ab?c', 'abbc'))
print(re.search('ab?c', 'abc'))

# | or
print(re.search('abc|012', '012'))

# () グループ
print(re.search('te(s|x)t', 'test'))

# . 任意の一文字
print(re.search('h.t', 'hot'))

# \ エスケープ
print(re.search('h\.t', 'h.t'))

# \w [a-zA-Z0-9_] 全てのアルファベット、数字およびアンダースコア
print(re.search('h\wt', 'h_t'))

# Challenge1
pattern_email = "^(19|20)[0-9]{2}/([1-9]|1[0-2])/([1-9]|1[0-9]|2[0-9]|3[0|1])$"
while True:
    dob = input("生年月日を入力してください。(yyyy/mm/dd）")
    result = re.search(pattern_email, dob)
    if result:
        print(f"{dob}は正しいフォーマットです。")
        break
    else:
        print(f"{dob}は正しくないフォーマットです。")


# Challenge2
pattern_email = "^(\w|\.|-)+@(\w|\.|-)+\.[a-zA-Z]{2,3}$"
while True:
    email = input("emailアドレスを入力してください。(example@yyyy.xx.dd）")
    result = re.search(pattern_email, email)
    if result:
        print(f"{email}は正しいフォーマットです。")
        break
    else:
        print(f"{email}は正しくないフォーマットです。")
