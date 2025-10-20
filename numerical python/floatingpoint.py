import numpy as np

np.random.seed(seed=1)

print(np.random.uniform(low =-1, high = 1,size =(3, 2)))

array = np.array([1,2,3,4,5])

print(array)

#example 2
rng = np.random.default.rng()
fruits = np.array(["apple", "orange","banana","coconut","pineapple"])
fruits = rng.choice(fruits, size = 3)
print(fruits)