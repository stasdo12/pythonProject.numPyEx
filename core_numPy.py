import numpy as np

# create array (one type)
array_numpy = np.array([1, 2, 3, 4])
print(array_numpy)
print(array_numpy.dtype)

array_numpy_with_different_type = np.array([1, 'Stan', True, 3])
print(array_numpy_with_different_type)  # Everything will be String
print(array_numpy_with_different_type.dtype)
# index call
print(array_numpy_with_different_type[1])
array_numpy_with_different_type[1] = '123'
print(array_numpy_with_different_type)

array_numpy_new = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
print(array_numpy_new[3])
# python create new array with values by index
print(array_numpy_new[[1, 1, 1, 1, 1, 1, 1, 1, 1]])
print(array_numpy_new[[True, True, False, False, False, True, True, True, True]])

# create a matrix 3x3 with method reshape
matrix_array = array_numpy_new.reshape(3, 3)
print(matrix_array[0][0])
