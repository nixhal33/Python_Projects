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
    # here this full_name_vehicle will give you direct all output as you can get by running the program
    
class ElectircCar(Vehicles):
    def __init__(self, brand, model,batterysize,fueltype,color):
        super().__init__(brand, model)    
        self.batterysize=batterysize
        self.fueltype=fueltype
        self.color=color


new_car=ElectircCar("BYD","MODEL PSY","150KWH","ELECTRIC","GREEN GOBLIN")
print(new_car.full_name_vehicle())