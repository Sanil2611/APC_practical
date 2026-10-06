# Problem Statement:
# Store marks of 10 students in a NumPy array. Calculate:
# Highest marks
# Lowest marks
# Average marks
# Median
# Standard deviation

import numpy as np

marks = np.array([78, 85, 92, 67, 88, 76, 95, 81, 73, 90])

print("Highest Marks:", np.max(marks))
print("Lowest Marks:", np.min(marks))
print("Average Marks:", np.mean(marks))
print("Median:", np.median(marks))
print("Standard Deviation:", np.std(marks))
