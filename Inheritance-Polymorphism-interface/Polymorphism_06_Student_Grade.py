# Problem Statement:
# Create a base class Student with a method calculate_grade(). Derive EngineeringStudent,
# MedicalStudent, and ManagementStudent. Override the method according to different grading criteria.

class Student:
    def calculate_grade(self):
        pass


class EngineeringStudent(Student):
    def calculate_grade(self):
        return "Engineering Grade: A"


class MedicalStudent(Student):
    def calculate_grade(self):
        return "Medical Grade: A+"


class ManagementStudent(Student):
    def calculate_grade(self):
        return "Management Grade: B"


students = [EngineeringStudent(), MedicalStudent(), ManagementStudent()]

for student in students:
    print(student.calculate_grade())
