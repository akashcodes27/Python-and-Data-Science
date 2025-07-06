
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

#Creating an array of zeroes and ones
# By default it uses float type for both ones and zeros

a1 = np.ones((4,5))
print(a1)

a2 = np.zeros((3,7))
print(a2)


# Creating an ndarray by specifying start, stop and step(gaps)
# But this only creates vectors (1-D numpy arrays)
# Format: start, stop, step
a3 = np.arange(2, 20, 2)
print(a3)

# We will now find out how we can generate 2-D numpy arrays by specifying start, stop, rows, columns
# Format: start, stop, size
a4 = np.random.randint(0, 30, size=(4,5))
print(a4)


# We can also generate a random 2-D numpy array of this format [0.0, 1.0) of float values
# We also specify the size which is basically rows and columns, and all values in this array will be between 0.0 and 1.0

random_arr = np.random.random((3, 6))
print(random_arr)


# All random numpy arrays we looked at so far:
# np.arange(start, stop, step): creates 1-D arrays
# np.random.randint(start, stop, size=(rows, cols)):  creates 2-D arrays with size
# np.random.random((rows, cols)): creates 2-D arrays within range [0.0, 1.0)


random_arr = np.random.rand(3,3)
print(random_arr)



# REMEMBER
# arange, random.randint together  (start, stop, step), (start, stop, size)
# random.random, random.rand together ((rows, cols)), (rows, cols)


# Lets now look at the concept of np.random.seed()
# np.random.seed() also produces random numbers. But it produces random numbers that stay constant.
# np.random.seed() is not directly used for generating random numbers, it is used more like a header before using other random functions

np.random.seed(0)
rand_arr = np.random.random((5,5))
print(rand_arr)

# Now if we print rand_arr, it gives us the same output everytime 


# Difference between Python Lists and Python arrays.

print("Lets take a look at python's lists")
py_list = [1,2,3,4] * 2
print(py_list)


print("lets take a look at python's arrays")
py_arr = np.array([1,2,3,4]) * 2
print(py_arr)

# So whats the difference: We can clearly observe that when we use * operation on python lists, it concatenates. but when we do * operation on python's numpy arrays, it multiples the constant to every value of the array



# Like how we create arrays of 0s and 1s.
np.ones((3,3))
np.zeros((3,3))
# We can also create arrays of 7s

arr1 = np.full((4,4), 8)
print(arr1)

arr2 = np.full((5,5), 3)
print(arr2)



# Tensors (Numpy arrays with more than 2 dimensions)
print("Now we are working with tensors")
arr1 = np.array([[[1,2,3], [4,5,6], [7,8,9]],
                 [[11,22,33], [44,55,66], [77,88,99]],
                 [[12,23,34], [45,56,67], [10,20,30]]])

print(arr1)

# Lets now take a look at the properties of numpy arrays
print(arr1.dtype)
print(arr1.size)
print(arr1.shape)
print(arr1.ndim)



# Some important Numpy array manipulation functions 

arr1 = np.arange(15)
print(arr1)


arr2 = arr1.reshape(3,5)
print(arr2)

arr3 = arr2.flatten()
print(arr3)

arr4 = arr2.ravel()
print(arr4)

# arange: we know what it does, it creates a vector with specified range and step
# reshape: it takes existing vector as input and changes its shape(adds rows and columns) to a 2-D array
# flatten: it takes a multi-dim tensor or matrice as input and converts it into a vector(1-D array)
# ravel: Does the same thing as flatten, but makes a mutation to exisiting array instead of creating a copy


# Transpose of a matrix: What is it? If we have a matrix, existing rows become new columns and existing columns become new rows
arr1 = np.arange(0, 40, 2)
print(arr1)

arr2 = arr1.reshape((4,5))
print(arr2)

# This is the transpose operation on matrix created by applying the reshape function to a 1D vector 
arr3 = arr2.T 
print(arr3)


# Slicing and indexing in Numpy 
arr1 = np.array([11,22,33,44,55,66,77,88,99])
print(arr1[2:7])
print(arr1[-4])
print(arr1[-2:-5:-1])   #When doing negative slicing, it is necessary to specify the negative step (-1),else by default arrays and lists both consider positive step movements