# Problem Statement:
# Create a 3D array containing integers from 1 to 27. Flatten the array and calculate:
# Sum
# Average
# Maximum
# Minimum

import numpy as np

arr = np.arange(1, 28).reshape(3, 3, 3)
flat = arr.flatten()

print("Flattened Array:", flat)
print("Sum:", np.sum(flat))
print("Average:", np.mean(flat))
print("Maximum:", np.max(flat))
print("Minimum:", np.min(flat))
