class MyClass:
    def __str__(self):
        return "MyClassの__str__"

mc = MyClass()
print(mc) # mc.__str__()
print(1) # 1.__str__()

# printableな性質（__str__()）を持っている
various_types = [1, "1", True, [1, 2, 3], (1,), {'1':1}, {1}]
for elem in various_types:
    print(elem) # .__str__()