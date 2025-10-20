import numpy as np

array = np.array([[1,2,3,4],
                  [5,6,7,8],
                  [9,10,11,12],
                  [13,14,15,16]])

# array [start:end:step]

print(array[0])
print(array[-1])
print(array[0:1])
print("========")
print(array[0:3])
print("========")
print(array[0:4:2])
print("========")
print(array[::2])
print("========")
print(array[::-2])
print("========")
print(array[::-1])

#column selection

print("========")
print(array[:,0])
print("========")
print(array[:,3])
print("========")
print(array[:,1:4])
print("========")
print(array[:,::-1])
print("========")
print(array[:,::2])
print("========")
print(array[:,1::2])
print("========")
print(array[:,::-2])
print("========")

#combining row amd column selection

print(array[0:2, 0:2])
print("========")
print(array[2:4, 2:])
print("========")
print(array[2:, 2:])
print("========")