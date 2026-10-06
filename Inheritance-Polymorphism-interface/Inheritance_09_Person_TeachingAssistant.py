# Problem Statement:
# Create a class Person. Derive Student and Faculty from Person. Create another class
# TeachingAssistant that inherits from both Student and Faculty. Display the details
# and demonstrate the use of multiple and hierarchical inheritance together.

class Person:
    def __init__(self, name):
        self.name = name


class Student(Person):
    def __init__(self, name, roll_no):
        super().__init__(name)
        self.roll_no = roll_no


class Faculty(Person):
    def __init__(self, name, subject):
        super().__init__(name)
        self.subject = subject


class TeachingAssistant(Student, Faculty):
    def __init__(self, name, roll_no, subject):
        Person.__init__(self, name)
        self.roll_no = roll_no
        self.subject = subject

    def display(self):
        print("Name:", self.name)
        print("Roll No:", self.roll_no)
        print("Subject:", self.subject)


ta = TeachingAssistant("Rahul", 101, "Python")
ta.display()
