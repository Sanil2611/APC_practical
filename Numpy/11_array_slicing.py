# Problem Statement:
# Create a NumPy array containing numbers from 1 to 20. Using slicing, display:
# First 5 elements
# Last 5 elements
# Alternate elements
# Elements in reverse order

import numpy as np

arr = np.arange(1, 21)

print("First 5 Elements:", arr[:5])
print("Last 5 Elements:", arr[-5:])
print("Alternate Elements:", arr[::2])
print("Reverse Order:", arr[::-1])
