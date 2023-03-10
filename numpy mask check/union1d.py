import numpy as np

# create two masked arrays
x = np.ma.array([1, 2, 3, 4], mask=[False, False, True, False])
y = np.ma.array([3, 4, 5, 6], mask=[True, False, False, False])

# find the union of the two arrays
union = np.ma.union1d(x, y)

# print the result
print(union)