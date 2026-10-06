# Problem Statement:
# Create a 4 × 4 NumPy array and write a program to:
# Display the first row
# Display the last column
# Display the diagonal elements
# Display the elements from the second and third rows

import numpy as np

arr = np.array([[1, 2, 3, 4],
                [5, 6, 7, 8],
                [9, 10, 11, 12],
                [13, 14, 15, 16]])

print("First Row:", arr[0])
print("Last Column:", arr[:, -1])
print("Diagonal Elements:", np.diag(arr))
print("Second and Third Rows:")
print(arr[1:3])
