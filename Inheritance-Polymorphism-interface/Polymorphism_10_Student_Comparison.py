# Problem Statement:
# Create a class Student containing the student's name and total marks. Overload the >
# and < operators to compare the marks of two students.

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def __gt__(self, other):
        return self.marks > other.marks

    def __lt__(self, other):
        return self.marks < other.marks


s1 = Student("Rahul", 450)
s2 = Student("Amit", 420)

print("Rahul has greater marks:", s1 > s2)
print("Rahul has lower marks:", s1 < s2)
