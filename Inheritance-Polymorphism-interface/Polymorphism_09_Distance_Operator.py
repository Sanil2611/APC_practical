# Problem Statement:
# Create a class Distance with feet and inches. Overload the + operator to add two
# distance objects and display the result in normalized form.

class Distance:
    def __init__(self, feet, inches):
        self.feet = feet
        self.inches = inches

    def __add__(self, other):
        total_inches = self.inches + other.inches
        feet = self.feet + other.feet + total_inches // 12
        inches = total_inches % 12
        return Distance(feet, inches)

    def display(self):
        print(self.feet, "feet", self.inches, "inches")


d1 = Distance(5, 8)
d2 = Distance(3, 7)

d3 = d1 + d2
d3.display()
