# Problem Statement:
# Create a base class Vehicle with attributes brand and model.
# Create a derived class Car with additional attributes fuel_type and price.
# Define methods to display vehicle details and calculate the discounted price of the car.

class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def display(self):
        print("Brand:", self.brand)
        print("Model:", self.model)


class Car(Vehicle):
    def __init__(self, brand, model, fuel_type, price):
        super().__init__(brand, model)
        self.fuel_type = fuel_type
        self.price = price

    def discounted_price(self, discount):
        return self.price - self.price * discount / 100

    def display(self):
        super().display()
        print("Fuel Type:", self.fuel_type)
        print("Price:", self.price)
        print("Discounted Price:", self.discounted_price(10))


car = Car("Toyota", "Glanza", "Petrol", 900000)
car.display()
