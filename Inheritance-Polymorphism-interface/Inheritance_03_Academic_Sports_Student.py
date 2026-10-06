# Problem Statement:
# Create two classes Academic and Sports. The Academic class should store marks
# obtained by a student, while the Sports class should store sports points.
# Create a class Student that inherits from both classes and calculates the student's
# overall performance.

class Academic:
    def __init__(self, marks):
        self.marks = marks


class Sports:
    def __init__(self, sports_points):
        self.sports_points = sports_points


class Student(Academic, Sports):
    def __init__(self, marks, sports_points):
        Academic.__init__(self, marks)
        Sports.__init__(self, sports_points)

    def overall_performance(self):
        return self.marks + self.sports_points

    def display(self):
        print("Academic Marks:", self.marks)
        print("Sports Points:", self.sports_points)
        print("Overall Performance:", self.overall_performance())


s = Student(85, 10)
s.display()
