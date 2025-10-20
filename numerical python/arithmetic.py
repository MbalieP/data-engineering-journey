import numpy as np

#Scalar arithmetic : lbra inear algebra term , meaning single value

array = np.array([1,2,3])

print(array)
print(array + 1)
print(array - 1)
print(array - 2)
print(array * 3)
print(array / 4)
print(array ** 5)

#Vectorized math functions: a vector is a single dimension 1d

array2 = np.array([1,2,3])
print(np.sqrt(array2))

array3 = np.array([1.01,2.5,3.99])
print(np.sqrt(array3))
print(np.round(array3))
print(np.floor(array3))
print(np.pi)

#exercise
radii = np.array([1,2,3])

print(np.pi * radii **2)

# element - wise arithmetic

array5 = np.array([1,2,3])
array6 = np.array([4,5,6])

print(array5 + array6)
print(array5 - array6)
print(array5 * array6)
print(array5 / array6)
print(array5 ** array6)

#comparison operators

scores = np.array([91, 55, 100, 73, 82, 64])

print(scores == 100)
print(scores >= 60)

scores[scores < 60] = 0
scores[scores > 60 & scores < 80] = 1
scores[scores > 80] = 2
print(scores)