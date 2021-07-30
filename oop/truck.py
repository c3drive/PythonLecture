from car import Car

class Truck(Car):

    def __init__(self, model_name, mileage, manufacturer, maxpile):
        super().__init__(model_name, mileage, manufacturer)
        self._maxpile = maxpile
        self._nowpile = 0

    # オーバーライド
    def gas(self):
        if self._nowpile > self._maxpile:
            print("重量オーバーなので走れません。")
            print(f"最低でも{self._nowpile - self._maxpile}kg降ろしてください。")
        else:
            super().gas()

    @property
    def nowpile(self):
        return self._nowpile

    @nowpile.setter
    def load(self, weight):
        if weight > 0:
            self._nowpile += weight
            print(f"{weight}kgの荷物を積みました。")
        else:
            if self._nowpile <= -weight:
                self._nowpile = 0
                print("全ての荷物を下ろしました。")
            else:
                self._nowpile += weight
                print(f"{weight}kgの荷物を下ろしました。")
        print(f"現在の積載量は{self._nowpile}kgです。")

        if self._nowpile > self._maxpile:
            print(f"最大積載量は、{self._maxpile}kgです。積載量がオーバーしています。")


suzuki = Truck("Suzuki GT", 5, "Suzuki", 10)
suzuki.gas()
suzuki.load = 9
suzuki.load = 9
suzuki.gas()