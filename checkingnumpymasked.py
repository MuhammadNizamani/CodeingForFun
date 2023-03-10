import numpy as np

# create a numpy array with some invalid values
x = np.array([1, 2, 3, -999, 5, -999, 7, 8, -999])

# create a mask array to indicate the invalid values
mask = x == -999

# create a masked array based on the original array and the mask
mx = np.ma.masked_array(x, mask)

# print the masked array
print(mx)

# compute the mean of the valid values in the array
mean = mx.mean()
print(mean)