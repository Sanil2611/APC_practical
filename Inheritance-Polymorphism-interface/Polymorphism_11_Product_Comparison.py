# Problem Statement:
# Create a class Product with product name and price. Overload the == and > operators
# to compare two products based on their prices.

class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __eq__(self, other):
        return self.price == other.price

    def __gt__(self, other):
        return self.price > other.price


p1 = Product("Laptop", 60000)
p2 = Product("Phone", 60000)

print("Prices are equal:", p1 == p2)
print("Laptop is costlier:", p1 > p2)
