# Problem Statement:
# Create a class Employee with attributes emp_id, name, and salary.
# Create a derived class Manager that inherits from Employee and contains
# an additional attribute department. Display all employee and manager details
# and calculate the manager's annual salary.

class Employee:
    def __init__(self, emp_id, name, salary):
        self.emp_id = emp_id
        self.name = name
        self.salary = salary

    def display(self):
        print("Employee ID:", self.emp_id)
        print("Name:", self.name)
        print("Salary:", self.salary)


class Manager(Employee):
    def __init__(self, emp_id, name, salary, department):
        super().__init__(emp_id, name, salary)
        self.department = department

    def annual_salary(self):
        return self.salary * 12

    def display(self):
        super().display()
        print("Department:", self.department)
        print("Annual Salary:", self.annual_salary())


m = Manager(101, "Rahul", 50000, "IT")
m.display()
