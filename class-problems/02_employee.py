# Problem Statement:
# Create a class Employee with attributes emp_id, name, and basic_salary.
# Define methods to calculate HRA, DA, and gross salary.

class Employee:
    def __init__(self, emp_id, name, basic_salary):
        self.emp_id = emp_id
        self.name = name
        self.basic_salary = basic_salary

    def calculate_hra(self):
        return self.basic_salary * 0.20

    def calculate_da(self):
        return self.basic_salary * 0.10

    def gross_salary(self):
        return self.basic_salary + self.calculate_hra() + self.calculate_da()

    def display(self):
        print("Employee ID:", self.emp_id)
        print("Name:", self.name)
        print("Basic Salary:", self.basic_salary)
        print("HRA:", self.calculate_hra())
        print("DA:", self.calculate_da())
        print("Gross Salary:", self.gross_salary())


e = Employee(101, "Rahul", 30000)
e.display()
