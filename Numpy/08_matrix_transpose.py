# Problem Statement:
# Create a 3 × 4 matrix and display its transpose.

import numpy as np

arr = np.array([[1, 2, 3, 4],
                [5, 6, 7, 8],
                [9, 10, 11, 12]])

print("Original Matrix:")
print(arr)

print("Transpose:")
print(arr.T)
