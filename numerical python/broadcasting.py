import numpy as np
# Broadcasting allows NumPy to perform operations on arrays
# with different shapes by virtually expanding dimensions
# so they match the larger array's shape

#the dimensions have the same size/
#or
#one of the dimensions has a size 1.

array1 = np.array([[1,2,3,4]])

array2 = np.array([[1],[2],[3],[4]])

print(array1.shape)
print(array2.shape)

print(array1 * array2)