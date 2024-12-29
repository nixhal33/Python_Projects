class Vehicles:
    total_vehicles=0 # this will count the no. of vehicles that i have added by accessing the vehicle class
    def __init__(self, brand, model): # this __init__ will help to encapsulate the methods
        self.__brand=brand
        self.__model=model
        Vehicles.total_vehicles += 1 # this will count the no. of vehicles 

    def get_brand(self):
        return self.__brand

    def set_brand(self, brand):
        self.__brand=brand

    def get_model(self):
        return self.__model

    def set_model(self, model):
        self.__model=model
    
    def full_detail(self):
        return f"Brand: {self.__brand} and Model: {self.__model}"

class ElectircCar(Vehicles):
    total_electric_car=0
    def __init__(self, brand, model,batterysize):
        super().__init__(brand, model)    
        self.batterysize=batterysize
        ElectircCar.total_electric_car+=1

    def get_batterysize(self):
        return self.__batterysize

    def set_batterysize(self, batterysize):
        self.__batterysize=batterysize


# here overidding the full_detail method to include the electric car details.
    def full_detail(self):
        return(
             f"Brand: {self.get_brand()}, Model: {self.get_model()}, "
        )

# updating some attributes using the setter method
new_car=ElectircCar("BYD","MODEL PSY","100kwh")
print(new_car.full_detail(),end='\n')

# updating some attributes using the setter method
new_vehicle=Vehicles("Mercedes","Benz")
print(new_vehicle.full_detail(),end='\n')

# again updating some attribs again using setter method
new_vehicle2=ElectircCar("Tesla","Model XXX","1009kwh") # maile ya electriccar wala class access gari ra xu maile tya attribute 3 ota deko thye but 2 ota matrai print gare vane error ayauxa so maile 3 otai attribute vako kura print garnu parxa 

print(new_vehicle2.full_detail(), end=' \n')

print("Total no. vehicles :")
print("Total no. of Vehicles :",Vehicles.total_vehicles)
print("Total no. of electric vehicles :",ElectircCar.total_electric_car)