import time

class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def create_from_dob(cls, name, year, month, date):
        today = time.localtime()
        age = today.tm_year - year - ((today.tm_mon, today.tm_mday) < (month, date))
        #if (today.tm_mon, today.tm_mday) < (month, date):
        #    age = today.tm_year - year - 1
        #else:
        #    age = today.tm_year - year

        return cls(name=name, age=age)

    @staticmethod
    def create_from_dob2(name, year, month, date):
        today = time.localtime()
        age = today.tm_year - year - ((today.tm_mon, today.tm_mday) < (month, date))
        return Person(name=name, age=age)

class Baby(Person):
    pass


john = Baby('John', 20)
emma = Baby.create_from_dob('Emma', 1983, 6, 18)
emily = Baby.create_from_dob2('Emily', 1983, 9, 18)

print(emma.name)
print(emma.age)
print(emily.age)
print(type(john))
print(type(emma))
# Babyから作っているのに、staticメソッドは直接Personから直接作ってしまうので
# staticメソッドは使わないようにする
print(type(emily))