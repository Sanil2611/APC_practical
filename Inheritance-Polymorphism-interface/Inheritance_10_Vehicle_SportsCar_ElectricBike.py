# Problem Statement:
# Create a base class Vehicle. Derive Car and Bike from Vehicle. Create a class SportsCar
# that inherits from Car and another class ElectricBike that inherits from Bike.
# Add suitable attributes and methods to demonstrate a combination of inheritance types.

class Vehicle:
    def __init__(self, brand):
        self.brand = brand


class Car(Vehicle):
    def drive(self):
        print(self.brand, "Car is driving")


class Bike(Vehicle):
    def ride(self):
        print(self.brand, "Bike is riding")


class SportsCar(Car):
    def race(self):
        print(self.brand, "Sports Car is racing")


class ElectricBike(Bike):
    def charge(self):
        print(self.brand, "Electric Bike is charging")


s = SportsCar("BMW")
e = ElectricBike("Ola")

s.drive()
s.race()
e.ride()
e.charge()
