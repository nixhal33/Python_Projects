class Car:
    def __init__(self, brand, model):
        self.brand=brand
        self.model=model

class ElectricCar(Car):
    def __init__(self, brand, model,battery_size):
        super().__init__(brand, model)
        self.battery_size=battery_size
        


my_new_car=ElectricCar("Tesla","Model X","100 KWH")
print(my_new_car.model)
print(my_new_car.brand)



merocar=Car("Mercedes","Silver Lightening")
print(merocar.brand)
print(merocar.model)


