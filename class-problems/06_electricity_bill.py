# Problem Statement:
# Create a class ElectricityBill containing consumer number, consumer name, and units consumed.
# Define a method to calculate the electricity bill according to different unit slabs.

class ElectricityBill:
    def __init__(self, consumer_number, consumer_name, units):
        self.consumer_number = consumer_number
        self.consumer_name = consumer_name
        self.units = units

    def calculate_bill(self):
        if self.units <= 100:
            bill = self.units * 1.50
        elif self.units <= 200:
            bill = 100 * 1.50 + (self.units - 100) * 2.50
        elif self.units <= 500:
            bill = 100 * 1.50 + 100 * 2.50 + (self.units - 200) * 4.00
        else:
            bill = 100 * 1.50 + 100 * 2.50 + 300 * 4.00 + (self.units - 500) * 6.00
        return bill

    def display(self):
        print("Consumer Number:", self.consumer_number)
        print("Consumer Name:", self.consumer_name)
        print("Units Consumed:", self.units)
        print("Electricity Bill: Rs.", self.calculate_bill())


e = ElectricityBill(1001, "Rahul", 350)
e.display()
