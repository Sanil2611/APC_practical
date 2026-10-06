# Problem Statement:
# Create a one-dimensional array containing numbers from 1 to 12.
# Reshape it into:
# 2 × 6 matrix
# 3 × 4 matrix
# 4 × 3 matrix

import numpy as np

arr = np.arange(1, 13)

print("2 x 6 Matrix:")
print(arr.reshape(2, 6))

print("3 x 4 Matrix:")
print(arr.reshape(3, 4))

print("4 x 3 Matrix:")
print(arr.reshape(4, 3))
