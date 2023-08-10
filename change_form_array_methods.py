import numpy as np

a = np.arange(10)
print(a)
a.shape = 5, 2
print(a)

b = a.reshape(10)
print(b)

a.shape = -1, 5
print(a)
print('---------------------')
c = np.arange(10)
print(c)
c.shape = -1, 2
print(c)
print(c.ravel())

a.shape = -1
print(a)

# resize method
print(c)
c.resize(2, 5)
print(c)
c.resize(3, 3, refcheck=False)
print(c)
c.resize(4, 5, refcheck=False)
print(c)

# transpire operation
new_array = np.array([(1, 2, 3), (1, 4, 9), (1, 8, 27)])
print(new_array)
print('---------------------')
q = new_array.T
print(q)

# transpire operation to vector, will be the same

vector_array = np.arange(1, 10)
print(vector_array)
vector_array.shape = 1, -1

q = vector_array.T
print(q)

# add and delete new rows (expand_dims(add), squeeze(delete) )

add_delete_array = np.arange(32).reshape(8, 2, 2)
print(add_delete_array)
print(add_delete_array.shape)
# add
add_delete_array1 = np.expand_dims(add_delete_array, axis=0)
print(add_delete_array1.shape)
# delete
add_delete_array1 = np.delete(add_delete_array, 0, axis=0)
print(add_delete_array1)

# if we need to delete all rows where only one element

add_delete_array = np.expand_dims(add_delete_array, axis=0)
print(add_delete_array.shape)
c = np.squeeze(add_delete_array)
print(c.shape)

# newaxis method
a = np.arange(1, 10)
b = a[np.newaxis, :, np.newaxis]
print(b)
