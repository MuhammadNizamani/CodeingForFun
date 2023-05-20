import numpy as np

arr = np.array([1, 2, 3, 3, 2, 1, 4, 5])
unique_arr, counts = np.unique(arr, return_counts=True, return_index=False, axis=None, )
print("Unique elements:", unique_arr)
print("Counts:", counts)

unique_all = np.unique(arr, return_counts=True, return_index=False, axis=None, 
                       return_inverse=False, )
print("Unique elements with counts and indices:", unique_all)