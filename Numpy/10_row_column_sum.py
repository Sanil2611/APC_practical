# Problem Statement:
# Create a 4 × 4 matrix and calculate the sum of each row and each column separately.

import numpy as np

arr = np.array([[1, 2, 3, 4],
                [5, 6, 7, 8],
                [9, 10, 11, 12],
                [13, 14, 15, 16]])

print("Row Sums:", np.sum(arr, axis=1))
print("Column Sums:", np.sum(arr, axis=0))
