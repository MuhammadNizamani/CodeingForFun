# In this example, we set return_inverse=True in the np.unique()
# function call. The resulting indices array shows the position of each element
# in the unique_arr array in the original input array arr.

import numpy as np

arr = np.array([1, 2, 3, 3, 2, 1, 4, 5])
unique_arr, counts, indices = np.unique(
    arr, return_counts=True, return_index=False, return_inverse=True)
print("Unique elements:", unique_arr)
print("Counts:", counts)
print("Indices of unique elements in original array:", indices)
