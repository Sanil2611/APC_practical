# Problem Statement:
# Create an array of 10 integers. Replace all elements greater than 50
# with 0 using NumPy Boolean indexing.

import numpy as np

arr = np.array([25, 60, 45, 75, 30, 90, 10, 55, 40, 80])

arr[arr > 50] = 0

print("Updated Array:", arr)
