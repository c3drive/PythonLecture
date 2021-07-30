class Person:

    def __init__(self, name):
        self.name = name
        self.__mymethod() # 継承先と同じメソッドと区別するため

    def mymethod(self):
        print("Person method is called")

    # def __mymethodとしてしまうと、Personのmymethodを呼びづらくなるため以下のようにする
    __mymethod = mymethod


class Baby(Person):
    def mymethod(self):
        print("Baby method is called")


ann_baby = Baby("ann")
ann_person = Person("ann")

ann_baby.mymethod()
ann_person.mymethod()