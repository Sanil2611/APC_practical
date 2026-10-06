# Problem Statement:
# Take marks of 20 students, calculate the class average and display
# the marks of students who scored above the average.

import numpy as np

marks = np.array([65, 78, 82, 55, 90, 72, 88, 61, 95, 70,
                  84, 76, 69, 91, 58, 80, 73, 87, 66, 93])

average = np.mean(marks)
above_average = marks[marks > average]

print("Class Average:", average)
print("Marks Above Average:", above_average)
