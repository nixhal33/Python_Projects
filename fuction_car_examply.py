# Inheritance completed!!

# Classes: Vehicles, ElectircCar
# Objects: new_car
# Attributes: brand, model, batterysize, fueltype, color
# Methods: full_name_vehicle(), calculate_volume()

class Vehicles:
    def __init__(self, brand, model):
        self.brand=brand
        self.model=model

    # this function i created here is i added a new functionality here where my_car method can access the function of the class vehicle while doing print(my_car.full_name_vehicle())
    def full_name_vehicle(self):
        return f"Brand: {self.brand},model: {self.model}, Battery-size: {self.batterysize}, Fuel-type: {self.fueltype}, Color: {self.color}"

    def calculate_volume(self):
        l=float(input("Enter the length of your car?"))
        b=float(input("Enter the breadth of your car?"))
        h=float(input("Enter the height of your car?"))
        volume=l*b*h
        return volume
    
class ElectircCar(Vehicles):
    def __init__(self, brand, model,batterysize,fueltype,color):
        super().__init__(brand, model)    
        self.batterysize=batterysize
        self.fueltype=fueltype
        self.color=color


new_car=ElectircCar("BYD","MODEL PSY","150KWH","ELECTRIC","GREEN GOBLIN")
print(new_car.full_name_vehicle())



# print(f"The model of {new_car.brand} is :", new_car.model)
# print(f"The color of the {new_car.brand} is :", new_car.color)
# print(f"The battery size of {new_car.brand} is :", new_car.batterysize)



# my_car=Vehicles("GMC","Black Lamborgini")
# print(my_car.full_name_vehicle())
# print('The volume of the car is :', my_car.calculate_volume())
