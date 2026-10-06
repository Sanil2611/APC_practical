# Problem Statement:
# Create a class MobilePhone with attributes brand, model, storage, and price.
# Define methods to display specifications and calculate the price after discount.

class MobilePhone:
    def __init__(self, brand, model, storage, price):
        self.brand = brand
        self.model = model
        self.storage = storage
        self.price = price

    def display_specifications(self):
        print("Brand:", self.brand)
        print("Model:", self.model)
        print("Storage:", self.storage)
        print("Original Price: Rs.", self.price)

    def price_after_discount(self, discount_percent):
        return self.price - (self.price * discount_percent / 100)


phone = MobilePhone("Samsung", "Galaxy A55", "256 GB", 40000)
phone.display_specifications()

discount = 10
print("Discount:", discount, "%")
print("Price After Discount: Rs.", phone.price_after_discount(discount))
