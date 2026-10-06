# Problem Statement:
# Create a class Student with attributes such as roll_no, name, and marks.
# Create objects for multiple students and display their details and percentage.

class Student:
    def __init__(self, roll_no, name, marks):
        self.roll_no = roll_no
        self.name = name
        self.marks = marks

    def display(self):
        print("Roll No:", self.roll_no)
        print("Name:", self.name)
        print("Marks:", self.marks)
        print("Percentage:", self.marks, "%")


s1 = Student(101, "Rahul", 85)
s2 = Student(102, "Amit", 78)

print("Student 1")
s1.display()

print("\nStudent 2")
s2.display()
