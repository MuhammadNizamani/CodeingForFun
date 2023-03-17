import numpy as np

# Two arrays with random data
x = np.array([1, 2, 3, 4, 5])
y = np.array([2, 4, 6, 8, 10])

# Compute the correlation matrix
corr_matrix = np.corrcoef(x, y)

print(corr_matrix)