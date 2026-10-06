# Problem Statement:
# Create a (2, 3, 4) array and calculate:
# Sum of all elements
# Sum of each layer
# Sum along rows
# Sum along columns

import numpy as np

arr = np.arange(1, 25).reshape(2, 3, 4)

print("Sum of All Elements:", np.sum(arr))
print("Sum of Each Layer:", np.sum(arr, axis=(1, 2)))
print("Sum Along Rows:", np.sum(arr, axis=2))
print("Sum Along Columns:", np.sum(arr, axis=1))
