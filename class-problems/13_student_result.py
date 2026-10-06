# Problem Statement:
# Create a class StudentResult with student name and marks in five subjects.
# Use a constructor to initialize the details.
# Define methods to calculate total, percentage, and grade.
# Implement a destructor to display a suitable message.

class StudentResult:
    def __init__(self, student_name, m1, m2, m3, m4, m5):
        self.student_name = student_name
        self.marks = [m1, m2, m3, m4, m5]

    def total(self):
        return sum(self.marks)

    def percentage(self):
        return self.total() / 5

    def grade(self):
        p = self.percentage()

        if p >= 90:
            return "A"
        elif p >= 80:
            return "B"
        elif p >= 70:
            return "C"
        elif p >= 60:
            return "D"
        else:
            return "F"

    def display(self):
        print("Student Name:", self.student_name)
        print("Marks:", *self.marks)
        print("Total:", self.total(), "/500")
        print("Percentage:", self.percentage(), "%")
        print("Grade:", self.grade())

    def __del__(self):
        print("StudentResult object destroyed.")


s = StudentResult("Rahul", 85, 78, 92, 88, 80)
s.display()
