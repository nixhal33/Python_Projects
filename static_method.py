class Car:
    def __init__(self, brand, model):
        self.brand=brand
        self.model=model

class ElectricCar(Car):
    def __init__(self, brand, model,battery_size):
        super().__init__(brand, model)
        self.battery_size=battery_size
        
    @staticmethod    # this declares the below below method to be a static method and no other object can access it ....
    def general_description():
        return "Electric Cars are the worst means of transport"


my_new_car=ElectricCar("Tesla","Model X","100 KWH")
print(my_new_car.model)
print(my_new_car.brand)
print(ElectricCar.general_description()) # this is how to access the static method... no need to make any object and access it...

merocar=Car("Mercedes","Silver Lightening")
print(merocar.brand)
print(merocar.model)

