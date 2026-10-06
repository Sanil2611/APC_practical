# Problem Statement:
# Create a 3D array of random integers between 1 and 100.
# Replace all values greater than 50 with 0.

import numpy as np

arr = np.random.randint(1, 101, size=(2, 3, 4))

print("Original Array:")
print(arr)

arr[arr > 50] = 0

print("Updated Array:")
print(arr)
