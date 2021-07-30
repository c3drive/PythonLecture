# 関数（function）
# 華氏から摂氏に変換する
fahrenheit = 72
celesius = (fahrenheit - 32) * 5 / 9
print(celesius)

# celesius = fahrenheit_to_celsius(fahrenheit)
def fahrenheit_to_celsius(fahrenheit):
    celesius = (fahrenheit - 32) * 5 / 9
    return celesius

celsius = fahrenheit_to_celsius(fahrenheit)
print(celsius)