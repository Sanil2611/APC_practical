# Problem Statement:
# Create two compatible matrices using NumPy and perform matrix multiplication
# using an appropriate NumPy function.

import numpy as np

a = np.array([[1, 2, 3],
              [4, 5, 6]])

b = np.array([[7, 8],
              [9, 10],
              [11, 12]])

result = np.matmul(a, b)

print("Matrix Multiplication:")
print(result)
