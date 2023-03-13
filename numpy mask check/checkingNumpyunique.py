# You can use the numpy.unique function with the return_counts
# and axis parameters to get unique elements and their respective counts
# along a particular axis of a numpy array. Here's an example:
import numpy as np

# Create a 2D numpy array
arr = np.array([[1, 2, 3], [2, 3, 4], [1, 2, 1]])

# Get unique elements and their respective counts along axis 0
unique_elements, counts = np.unique(arr, return_counts=True, axis=0)

# Print the unique elements and their counts
print("Unique elements:")
print(unique_elements)
print("Counts:")
print(counts)


# In this example, the arr array contains three rows of numbers.
# We want to find the unique rows and their respective counts along the 
# vertical axis (axis 0). To do this, we pass return_counts=True and axis=0 
# to the np.unique function. The resulting unique_elements array contains the
# unique rows, and the counts array contains the number of occurrences of each 
# unique row