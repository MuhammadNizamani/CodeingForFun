import numpy as np
c = memoryview(np.void(4)) == np.void(4)  # this works
print(np.void(4), c)
print(memoryview(np.void(34)))
# Create a bytes object
data = b"hello world"

# Create a memoryview object from the bytes object
mv = memoryview(data)
print(type(mv))
