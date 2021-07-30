class Car(object):

    def __init__(self, model_name, mileage, manufacturer):
        self.model_name = model_name
        self.mileage = mileage
        self.manufacturer = manufacturer

    def gas(self):
        print("{0.manufacturer}の{0.model_name}(燃費：{0.mileage}）アクセス全開".format(self))

    def breakes(self):
        print(f"{self.manufacturer}の{self.model_name}(燃費:{self.mileage}),ブレーキ！!!")

if __name__ == "__main__":
    conti_gt = Car("Bentley Continental GT", 4, "Bentley")
    conti_gt.gas()
    conti_gt.breakes()