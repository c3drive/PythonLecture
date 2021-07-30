class Person(object):

    num_legs = 2
    count = 0
    # constructor(__new__)
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
        # インスタンスが作られるたびに更新される
        Person.count += 1

    def walk(self):
        print(f"{self.name} is walking...with {Person.num_legs} legs")

    def run(self):
        print(f"{self.name} is running")


john = Person("John", 28, "male")
print(Person.count)
taro = Person("Taro", 18, "male")
print(Person.count)
emma = Person("Emma", 40, "female")
print(Person.count)

# インスタンス変数
# [.]に続けてアクセス可能
print(john.name)
print(john.age)
print(john.gender)

print(taro.name)
print(taro.age)
print(taro.gender)

taro.age = 19
print(taro.age)

# インスタンスメソッド
john.walk()
emma.walk()

print(john.num_legs)
print(taro.num_legs)

# クラス変数の更新はバグの元なのでしない
john.num_legs = 3
print(john.num_legs)
print(taro.num_legs)