# Problem Statement:
# Create a base class Employee with a method calculate_salary(). Derive Manager, Developer,
# and Tester classes. Override the method in each class to calculate salary according to
# the employee's role.

class Employee:
    def calculate_salary(self):
        pass


class Manager(Employee):
    def calculate_salary(self):
        return 50000 + 15000


class Developer(Employee):
    def calculate_salary(self):
        return 40000 + 8000


class Tester(Employee):
    def calculate_salary(self):
        return 35000 + 5000


employees = [Manager(), Developer(), Tester()]

for employee in employees:
    print("Salary:", employee.calculate_salary())
