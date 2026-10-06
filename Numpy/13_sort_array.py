# Problem Statement:
# Create an unsorted NumPy array and display it in:
# Ascending order
# Descending order

import numpy as np

arr = np.array([45, 12, 78, 23, 9, 56, 34])

print("Ascending Order:", np.sort(arr))
print("Descending Order:", np.sort(arr)[::-1])
