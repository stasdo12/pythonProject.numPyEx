import numpy as np

a = np.arange(0.1, 1, 0.1)
# if we need to know data type
print(a.dtype)
# change type in out array
a.dtype = np.int8()
print(a.size)
a.dtype = np.float64()
print(a)
print(a.itemsize)
print(a.size * a.itemsize)

b = np.ones((3, 4, 5))
print(b)
print(b.ndim)
print(b.shape)
b.shape = 60
print(b)

z = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
b = z.view()
print(b)
z.shape = 3, 3
print(b)
