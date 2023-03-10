import numpy as np

# create a masked array
x = np.ma.array([1, 2, 3, 4, 5], mask=[False, False, True, False, True])

# test for membership of values
mask = np.ma.isin(x, [2, 4, 6,76])

# print the result
print(mask)