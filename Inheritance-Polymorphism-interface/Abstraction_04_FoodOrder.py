# Problem Statement:
# Create an abstract class FoodOrder with abstract methods calculate_bill() and
# delivery_charge(). Derive RestaurantOrder and HomeDeliveryOrder and implement
# the methods appropriately.

from abc import ABC, abstractmethod

class FoodOrder(ABC):
    @abstractmethod
    def calculate_bill(self):
        pass

    @abstractmethod
    def delivery_charge(self):
        pass


class RestaurantOrder(FoodOrder):
    def __init__(self, amount):
        self.amount = amount

    def calculate_bill(self):
        return self.amount

    def delivery_charge(self):
        return 0


class HomeDeliveryOrder(FoodOrder):
    def __init__(self, amount):
        self.amount = amount

    def calculate_bill(self):
        return self.amount

    def delivery_charge(self):
        return 50


orders = [RestaurantOrder(500), HomeDeliveryOrder(500)]

for order in orders:
    print("Bill:", order.calculate_bill())
    print("Delivery Charge:", order.delivery_charge())
