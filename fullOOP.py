# Base Class/parent class
class Vehicle:
    # Constructor for Encapsulation (attributes are private)
    def __init__(self, brand, model, fuel_type):
        self.__brand = brand  # Private attribute
        self.__model = model  # Private attribute
        self.__fuel_type = fuel_type  # Private attribute

    # Getters and Setters for Encapsulation
    def get_brand(self):
        return self.__brand

    def set_brand(self, brand):
        self.__brand = brand

    def get_model(self):
        return self.__model

    def set_model(self, model):
        self.__model = model

    def get_fuel_type(self):
        return self.__fuel_type

    def set_fuel_type(self, fuel_type):
        self.__fuel_type = fuel_type

    # Method to be overridden (Polymorphism)
    def vehicle_description(self):
        return f"Brand: {self.__brand}, Model: {self.__model}, Fuel Type: {self.__fuel_type}"

    # Static Method (Abstraction)
    @staticmethod
    def general_info():
        return "Vehicles are used for transportation."

# Subclass 1
class Car(Vehicle):
    def __init__(self, brand, model, fuel_type, seating_capacity):
        super().__init__(brand, model, fuel_type)  # Call the parent constructor
        self.seating_capacity = seating_capacity  # New attribute specific to Car

    # Overriding the vehicle_description method (Polymorphism)
    def vehicle_description(self):
        return (
            f"Car - Brand: {self.get_brand()}, Model: {self.get_model()}, "
            f"Fuel Type: {self.get_fuel_type()}, Seating Capacity: {self.seating_capacity}"
        )

# Subclass 2
class ElectricCar(Vehicle):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model, "Electric")  # Set fuel type as "Electric"
        self.battery_size = battery_size  # New attribute specific to ElectricCar

    # Overriding the vehicle_description method (Polymorphism)
    def vehicle_description(self):
        return (
            f"Electric Car - Brand: {self.get_brand()}, Model: {self.get_model()}, "
            f"Battery Size: {self.battery_size}"
        )

    # Overriding the static method (Polymorphism)
    @staticmethod
    def general_info():
        return "Electric Cars run on batteries and are eco-friendly."

# Example Usage
# 1. Encapsulation with Getters and Setters
vehicle = Vehicle("Generic Brand", "Model X", "Diesel")
print(vehicle.vehicle_description())  # Access method
vehicle.set_brand("Updated Brand")  # Modify using setter
print(vehicle.vehicle_description())
print(isinstance(vehicle,ElectricCar))



# 2. Inheritance with Car
car = Car("Toyota", "Corolla", "Petrol", 5)
print(car.vehicle_description())  # Polymorphism in action


# 3. Polymorphism with ElectricCar
electric_car = ElectricCar("Tesla", "Model S", "100 kWh")
print(electric_car.vehicle_description())  # Polymorphism in action

# 4. Static Method and Polymorphism
print(Vehicle.general_info())  # Static method in base class
print(ElectricCar.general_info())  # Overridden static method in child class


"""
OOP Concepts in This Code
1. Encapsulation

    What: Wrapping data (attributes) and methods into a single unit.
    Where in the code:
        Private attributes in the Vehicle class (__brand, __model, __fuel_type).
        Getter and Setter methods (get_brand, set_brand, etc.) allow controlled access to private data.

2. Inheritance

    What: Child classes inherit properties and methods from the parent class.
    Where in the code:
        Car and ElectricCar inherit from Vehicle.
        Both child classes reuse and extend the functionality of the Vehicle class.

3. Polymorphism

    What: The ability of different objects to respond to the same method call in their own way.
    Where in the code:
        The vehicle_description method is overridden in Car and ElectricCar to provide specific details.
        The static method general_info() behaves differently for Vehicle and ElectricCar.

4. Abstraction

    What: Hiding implementation details and exposing only essential functionalities.
    Where in the code:
        The general_info() static method provides an abstract concept about vehicles without dealing with specific details.


"""