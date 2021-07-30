class Person:

    def __init__(self, name, age):
        self.name = name
        self._age = age

    def get_age(self):
        print("get_age called")
        return self._age

    def set_age(self, age):
        print("set_age called")
        if age < 0:
            print("0以上の値を入れてください")
        else:
            self._age = age

    # propertyビルトインファンクション
    age = property(get_age, set_age)

john = Person("John", 19)
print(john.age)
john.age = -10