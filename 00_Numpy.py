
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


# Slicing and indexing in matrices
arr1 = np.array([[1,2,3,4], [5,6,7,8], [11,22,33,44]])
print(arr1)
print(arr1[2, 3])    #Does normal indexing, row of index 2, column of index 3
print(arr1[:, 2])   #Lets say we want to retrieve a specific column(not row, not any element, but an entire column)
print(arr1[1 , :])  #Retrives row of index = 1 (only row, not column)

#Sorting Numpy Arrays (vectors)
arr1 = np.array([9, 12, 4, 20, 8, 3, 30])
print(np.sort(arr1))


arr2 = np.array([[4,3,2,1], [44,33,22,11], [8,7,6,5]])
print(np.sort(arr2, axis=0))   #Does column sorting (more useful)
print(np.sort(arr2, axis=1))   #Does row sorting

# Lets see how we can apply filter to a numpy array
print("Applying Filter")
arr1 = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
mask = arr1 > 5  
filtered_arr = arr1[mask]
print(filtered_arr)


arr2 = np.array([0,1,2,3,4,5,6,7,8,9])
new_arr2 = arr2[arr2 % 2 == 0]
print(new_arr2)

# Fancy Indexing
print("Lets see fancy indexing")
arr1 = np.array([11,22,33,44,55,66,77])
arr2 = [0, 2, 4]

print(arr1[arr2])
# We have defined one numpy array and one list. The numpy array contains all elements, the list contains all the indices
# We pass the list in the numpy array, and we obtain the elements stored at the indices of the list 

# Applying conditional by using np.where and mask filter
arr1 = np.array([12,23,34,45,56,67,78,89])
arr2 = arr1[np.where(arr1 > 23)]
arr3 = arr1[arr1 > 56]
print(arr1)
print(arr2)
print(arr3)
# This was like using WHERE clause in SQL



# Now we will see something similar to using UPDATE, SET, WHERE of SQL 
# So basically, we will apply Conditional as well as Manipulation 
print("Conditional and Data Manipulation")
arr1 = np.array([1,2,3,4,5,6,7,8])
# Weird and confusing syntax below 
print(arr1[np.where(arr1>3)])    #when we applying only conditional, this is the syntax
print(np.where(arr1>3, arr1*2, arr1))  #when we applying conditional as well as Manipulation, this is the syntax
# What this means, for elements that satisfy arr1>3 : action: arr1*2
#                  for elements that dont satisfy arr1>3 : action: arr1

# More intuitive example to understand the concept:
arrr1 = np.random.randint(0, 30, size=(5,7))
print(arrr1)
print(np.where(arrr1<15, False, True))
# This sets numbers less than 15 to False and numbers greater than or equal to 15 to True


# Adding or removing data

# When we perform '+' operation with python lists
# It concatenates content from both the arrays
l1 = [1,2,3,4]
l2 = [1,2,3,4]
print(l1+l2)


# When we perform '+' operation with numpy arrays 
# It does arithmetic addition of same index elements from both arrays
a1= np.array([1,2,3,4])
a2 = np.array([5,6,7,8])
print(a1+a2)

# But lets say we want to achieve concatenation with numpy arrays and not arithmetic addition
print(np.concatenate((a1, a2)))

a1 = np.array([1,2,3,4,5,6,7,8])
print(a1.shape)    #Shows number of (columns,)
a2 = np.random.rand(3,4)
print(a2)
print(a2.shape)   #Shows number of (rows, columms)

# Lets compare compatibility of different numpy arrays
a1 = np.array([1,2,3,4])
a2 = np.array([1,2,3,4,5,6,7])
print(a1.shape == a2.shape)  #Returns false as its obvious that their shape is different cuz diff number of cols 

# Lets explore vstack, what does it do?
a1 = np.array([[1,2,3,4], [5,6,7,8]])
a2 = np.array([[11,22,33,44]])

print(a1)
result_arr = np.vstack((a1, a2))
print(result_arr)
# As we can observe clearly we have integrated a new row to our 2-dimensional array, before its shape for (2,4), now its shape is (3,4)

# Lets say in this resulting array, we want add a new column
a3 = np.array([[69], [69], [69]])    #But make sure the new elements we are addin must be provided exactly in the same format of arrays as the arrays were initially created in 
result_arr = np.hstack((result_arr, a3))
print(result_arr)


a1 = np.array([1,2,3,4,5,6,7,8])
new_arr = np.delete(a1, 3)     #Deletes element at specified index and generates the resulting array
print(new_arr)    
# Format for delete function: np.delete(array, index)


# Advanced Operation with Business Example 
# [restaurant id, 2021, 2022, 2023, 2024]    Sales of different restaurants in different years 
sales_data = np.array([
    [1, 150000, 180000, 220000, 250000],
    [2, 120000, 140000, 160000, 190000],
    [3, 200000, 230000, 260000, 300000],
    [4, 180000, 210000, 240000, 270000],
    [5, 160000, 185000, 205000, 230000],
])

print(sales_data)
print(sales_data.shape)

print("Lets perform some operations on the matrix data we have over here")
# Lets quickly understand slicing, indexing, column retrival even better
print(sales_data[0 : 3])   #Works just like a dataframe
print(sales_data[3])
print(sales_data[1,3])  # 1 navigates rows, 3 navigates columns of that specific row and final result is a single value
print(sales_data[:, 3])   # considers all rows, returns a column of values(considering all rows)
print(sales_data[3 , :])   #Same as sales_data[3], navigates to row with index 3, and considers all columns for that specific row
print(sales_data[:, 1:])  #-> : considers all rows, 1: considers columns from index 1


# Now we take a look at some aggregate functions, we can change how we wish to do the aggregation
# Lets now calculate Total revenue for each year. We shall do this by doing: using sum() function and performing Column Slicing
result_arr = np.sum(sales_data[:, 1:], axis=0)  #This gets id of id column, as we dont wanna sum the ids
print(result_arr)

print(np.min(sales_data[:, 1:], axis=1))    #When you change axis from 0 to 1, just flip the axis from row to column

# When do we change between rows and columns: Depends on what kind of problem you are solving
# If lets say rows portray:
# id ,  Year1  ,  Year2  ,  Year3  ,  Year4
# And if we want to find restaurant with max revenue from every year 


# If lets say columns potray
# Cafe1
# Cafe2
# Cafe3
# Cafe4
# And if we want to find max revenue made by every restaurant



sales_data2 = np.array([
    [0, 100, 200, 300, 400, 500],
    [1, 10, 20, 30, 40, 50],
    [2, 11, 22, 33, 44, 55]
])

result = np.cumsum(sales_data2[:, 1:], axis=1)
print(result)
# Does side by side horizontal addition of values excluding the id column

result2 = np.cumsum(sales_data2[:, 1:], axis=0)
print(result2)
# Does vertical addition of values excluding the id column

# Lets take a simpler example
arr1 = np.array([
    [1, 1, 3, 5, 8],
    [2, 4, 8, 9, 2],
    [3, 8, 2, 6, 4],
    [4, 8, 7, 5, 1]
])

# We took mean or average
print(np.mean(arr1[: , 1:], axis=0))

# Then we took cumsum(cumulative sum)
print(np.cumsum(arr1[:, 1:], axis=0))
cumsum = np.cumsum(arr1[:, 1:], axis=0)

# Now we shall take the average of each cumsum
print(np.mean(cumsum, axis=0))


# Now lets do some plotting: figure, plot, title, xlabel, ylabel
# figure contains dimensions
# plot contains the code for aggregate function
# title contains the title text we want for the graph
# xlabel contains text we want for the x-axis
# ylabel contains the text we want for the y-axis

# import matplotlib as plt

# plt.figure(figsize=(10, 6))
# plt.plot(np.mean(cumsum, axis=0))
# plt.title("Average of cumulative values")
# plt.xlabel("X-axis")
# plt.ylabel("y-axis")
# plt.show()
# I am not sure why its not running, we shall figure it out in matplotlib module, but for now just remember the syntax


# Lets look at some vector operations 
vec1 = np.array([1, 2, 3, 4, 5, 6])
vec2 = np.array([9, 8, 7, 6, 5, 4])
vecsum = vec1 + vec2
print(vecsum)

vecprod = vec1 * vec2 #Performs mathematical vector multiplication
print(vecprod)

# We can also calculate the mathematical dot product
dotprod = np.dot(vec1, vec2)
print(dotprod)