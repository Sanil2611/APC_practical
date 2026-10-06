# Problem Statement:
# Create a base class Person with a method display_role(). Derive Student, Faculty,
# and Administrator. Override the method to display the respective role. Store all
# objects in a list and invoke the same method using a loop.

class Person:
    def display_role(self):
        pass


class Student(Person):
    def display_role(self):
        print("Role: Student")


class Faculty(Person):
    def display_role(self):
        print("Role: Faculty")


class Administrator(Person):
    def display_role(self):
        print("Role: Administrator")


people = [Student(), Faculty(), Administrator()]

for person in people:
    person.display_role()
