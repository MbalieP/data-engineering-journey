import numpy as np

array = np.array('A')
print(array.ndim)
print(array.shape)

array = np.array([1,3,5])
print(array.ndim)
print(array.shape)

array = np.array([[1,3,5],[1,3,5],[1,3,5]])
print(array.ndim)
print(array.shape)

array = np.array([[[1,3,5],[1,3,5],[1,3,5]],
                  [[1,3,5],[1,3,5],[1,3,5]],
                  [[1,3,5],[1,3,5],[1,3,5]]])
print(array.ndim)
print(array.shape)

array = np.array([[["A","B","C"],["D","E","F"],["G","H","I"]],
                  [["J","K","L"],["M","N","O"],["P","Q","R"]],
                  [["S","T","U"],["V","W","X"],["Y","Z"," "]]])
print(array.ndim)
print(array.shape)
print(array[2][0][0]) # chain idexing
print(array[0,0,2]) # multi dimensional indexing

word = array[2,0,0] + array[1,1,0] + array[0,0,0]
print(word)