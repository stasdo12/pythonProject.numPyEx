import numpy as np

# first method

first_array = np.array([1, 2, 3, 4], 'str_')
print(first_array)

# if we need to check all data type
print(np.sctypeDict.keys())

# most popular types
'''
bool_
int_
int8
int16
int32
int64
float
float4
float16
float32
complex64
str
'''

complex_number = np.complex64(10)
print(complex_number)

int_number = np.int16(10.5)
print(int_number)

# arguments for np.array()  - tuple or list all other type will be a one object
array_new = np.array((1, 2, 3))
print(array_new)
array_new_string = np.array("Hello")
print(array_new_string)

# if we need to create a matrix
matrix_array = np.array([[1,2,3], [4,5,6], [7,8,9]])
print(matrix_array)
print('----------------------')
matrix_array_third = np.array([[[1,2],[3,4]], [[5,6], [7,8]],[[9,10], [11,12]]])
print(matrix_array_third)
print('----------------------')
print(matrix_array_third[0][0][0])