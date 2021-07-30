class MyClass:

    classmethod_count = 0

    # selfを使っていないのでwarningが出ている（static）にすべき
    def mymethod(self):
        print("This is nomal method")

    @staticmethod
    def mystaticmethod():
        print("This is staticmethod")

    @classmethod
    def myclassmethon(cls):
        cls.classmethod_count += 1
        print(f"This is classmethod and now the count id {cls.classmethod_count}")

c = MyClass()
c.mymethod()
MyClass.mystaticmethod()
MyClass.myclassmethon()
MyClass.myclassmethon()