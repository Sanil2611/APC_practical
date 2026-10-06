# Problem Statement:
# Create a random 3D NumPy array of shape (3, 4, 5). Flatten it and display only
# the elements that are:
# Greater than 50
# Even numbers
# Less than the average value

import numpy as np

arr = np.random.randint(1, 101, size=(3, 4, 5))
flat = arr.flatten()
average = np.mean(flat)

print("Random 3D Array:")
print(arr)
print("Elements Greater Than 50:", flat[flat > 50])
print("Even Numbers:", flat[flat % 2 == 0])
print("Elements Less Than Average:", flat[flat < average])
