class Duck:
    """
    This a class for Duck.

    Attributes:
        name(str): the name of the duck

    Methods:
        walk: print ***
        quack: print **
        fly: ***
    """
    def __init__(self, name):
        """
        The constructor for Duck clask
        :param name: the name of the duck
        """
        self.name = name

    def walk(self):
        print("walking..")

    def quack(self):
        print("quack quack...")

    def fly(self):
        print("flying..")

class Penguin:
    def __init__(self, name):
        self.name = name

    def walk(self):
        print("walking..")

    def quack(self):
        print("quack quack...")

    def swim(self):
        print("swimming..")

def walk_and_quack(duck):
    duck.walk()
    duck.quack()

if __name__ == "__main__":
    help(Duck)
    help(Duck.__init__)
    print(Duck.__init__.__doc__)
    donald = Duck("Donald")
    pingu = Penguin("pingu")
    #donald.walk()
    #donald.quack()
    duck_list = [donald, pingu]
    for duck in duck_list:
        walk_and_quack(duck)