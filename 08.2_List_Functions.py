# List is an orderred collection of items that is mutable. List can store any type of datatypes. Less memory and performance effecient as compared to the tuples. 



# Creating a list
my_list = [10, "Hello", 4.16, "How are you", 56, 99, 209]
print(my_list)



# Accessing the list
print(my_list[2])
print(my_list[0])
print(my_list[3])
print(my_list[-1])    #returns the last element of the list 

# Modifying a value in list
my_list[2] = "This is modified"
print(my_list)



# Lists in python are dynamic, elements can be added or removed
my_list.append("This will be at last")
my_list.insert(2, 2222)          #this adds specified element at mentioned index 
print(my_list)


# Elements can also be removed from lists in python
my_list.pop()
my_list.remove("Hello")
print(my_list)



# List Slicing
numsList = [11,22,33,44,55,66,77,88, 99, 119, 129]
print(numsList[2:8])
print(numsList[:4])
print(numsList[4:])
print(numsList[::-1])    #Reverses the list 



# We can also have a list of list, it is called a "matrix"
matrix = [
    [1,2,4],
    [11,22,33],
    [12,34,56]
]

print(matrix)



# List Comprehension
squareList = [x**2 for x in range(1,7)]
print(squareList)


evenList = [x for x in range(1,5) if x%2 == 0 ]
print(evenList)



#Sorting and reversing
nums1 = [11,22,33,44,55,66,77,88]
nums1.reverse()
print(nums1)

nums2 = [54,23,7,1,45,67]
nums2.sort()
print(nums2)

