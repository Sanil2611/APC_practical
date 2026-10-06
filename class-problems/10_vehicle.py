# Problem Statement:
# Create a class Vehicle containing vehicle number, model, rental rate, and availability.
# Implement methods to rent and return a vehicle and calculate rental charges based on the number of days.

class Vehicle:
    def __init__(self, vehicle_number, model, rental_rate):
        self.vehicle_number = vehicle_number
        self.model = model
        self.rental_rate = rental_rate
        self.available = True

    def rent_vehicle(self):
        if self.available:
            self.available = False
            print("Vehicle rented successfully.")
        else:
            print("Vehicle is not available.")

    def return_vehicle(self, days):
        if not self.available:
            charges = self.rental_rate * days
            self.available = True
            print("Vehicle returned successfully.")
            print("Rental Charges: Rs.", charges)
        else:
            print("Vehicle was not rented.")

    def display(self):
        print("Vehicle Number:", self.vehicle_number)
        print("Model:", self.model)
        print("Rental Rate/Day: Rs.", self.rental_rate)
        print("Available:", "Yes" if self.available else "No")


v = Vehicle("MH10AB1234", "Swift", 1500)
v.display()
v.rent_vehicle()

days = int(input("Enter number of rental days: "))
v.return_vehicle(days)
v.display()
