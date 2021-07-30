class Animal:
    def __init__(self, name):
        self.name = name

    def walk(self):
        print(f"{self.name} is walking")

class Dog(Animal):
    def bark(self):
        print(f"{self.name} is barking")

def walk_with_me(animal: Animal) -> None:
    # Dogからwalkが呼ばれたとき実行されなくなってしまう
    # if type(animal) is Animal:

    # インスタンスの型をチェック。これでもいいがパイソニックではない
    # if isinstance(animal, Animal):

    # よりパイソニックなコード（振る舞い＝methodがあるかを確認する）
    method = getattr(animal, 'walk', None)
    if callable(method): # 呼べるかどうか
        animal.walk()
    else:
        raise TypeError(f"{type(animal).__name__}は散歩できません")

if __name__ == "__main__":
    pochi = Dog("Pochi")
    walk_with_me(pochi)
    walk_with_me("pochi")