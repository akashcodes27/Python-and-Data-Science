
import numpy as np

# 1-D array
a1 = np.array([1,2,3,4,5,6,7,8])
print(a1)


# 2-D array 
a2 = np.array([[1,2,3,4,5],[11,22,33,44,55],[10.1, 20, 30, 40, 50]])
print(a2)



# Gives us number of elements in a vector. a 1-d array is called a vector
print(a1.shape)

# Gives us the number of rows and columns. a 2-d array is called a matrix
print(a2.shape)

# Gives us the number of dimensions in the a1 vector
print(a1.ndim)


# Gives us the number of dimensions in the a2 matrix 
print(a2.ndim)


# Tells us the datatype
print(a1.dtype)
print(a2.dtype)


# Tells us the datastructure, which is obviously the ndarray 
print(type(a1))
print(type(a2))