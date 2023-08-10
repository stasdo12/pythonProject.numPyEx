import numpy as np

# matrix with 10 zero

matrix_with_zero = np.array([0] * 10)
print(matrix_with_zero)

a = np.array([1] * 10)
print(a)

# create array with list comprehension
array_comprehension = np.array([x for x in range(21)])
print(array_comprehension)

'''
np.empty(return a new empty array)
np.eye(N, M=None) (return array NxM)
np.identity(n. ...) (return new array nxn)
np.ones(shape, ...) (return array with all one values, and type)
np.zeros(shape, ...)(return array with all zero values, and type)
np.full(shape, value,...) (return array with our size, and type with our values)
'''

array_empty = np.empty(20)
print(array_empty)
array_eye = np.eye(3, 3)
print(array_eye)
array_identity = np.identity(5)
print(array_identity)
print('---------------------')
array_ones = np.ones(5, 'float64')
print(array_ones)
print('---------------------')
array_zeros = np.zeros(5, 'float64')
print(array_zeros)
print('---------------------')
array_full = np.full((3, 2), -1)
print(array_full)
print('---------------------')
# mat , diag, tri, vander
# if we want to create matrix by str
string_matrix = np.mat('1,2,3,4')
print(string_matrix)
print('---------------------')
string_matrix1 = np.mat('1,2;3,4')
print(string_matrix1)
print('---------------------')
diag_matrix = np.diag([1, 2, 3])
print(diag_matrix)
print('---------------------')
tri_matrix = np.tri(4)
print(tri_matrix)
print('---------------------')
vander_matrix = np.vander([1, 2, 3])
print(vander_matrix)
print('---------------------')
# arange, linspace, logspace, geomspace, meshgrid, mgrid, ogrid
array_arange = np.arange(0, np.pi, 0.1)
print(array_arange)
# if we need to find cos
print(np.cos(array_arange))
print('---------------------')
linspace_array = np.linspace(1, 10, 3)
print(linspace_array)
print('---------------------')
logspace_array = np.logspace(0, 1, 4)
print(logspace_array)
print('---------------------')
geomspace_array = np.geomspace(1, 16, 5)
print(geomspace_array)

print('---------------------')
# copy method
copy_array = np.copy(geomspace_array)
print(copy_array)

new_array = np.array([1, 2, 3])
print(new_array)


# from function method
def getRange(x, y):
    return 100 * x + y


print('---------------------')
after_func_array = np.fromfunction(getRange, (2, 2))
print(after_func_array)


after_func_array1 = np.fromfunction(lambda x,y: 100*x+y,  (2, 2))
print(after_func_array1)

# from iter method
a = np.fromiter("hello", dtype='U1')
print(a)

# from string method

b = np.fromstring('1, 2, 3,', dtype='int16', sep=',')
print(b)







