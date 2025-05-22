

# Write a program to calculate SUM of all elements in the list:


numbers = [5, 10, 15, 20]

sum = 0

for item in numbers:
    sum = sum + item 

print(f"The total sum is {sum}")



#---------------------------------------------------------------------------------------------------------------------------------


# 2. Find Maximum Element (Without using max())

numbers = [45, 1, 145, 3, 5]


largest = 0
for num in numbers:
    if num > largest:
        largest = num

print(largest)

print(f"The largest element of list is {largest}")

# How to remember it:
# You declare and initialize a variable, and keep updating it to the largest value as you iterate through the list. 


#-------------------------------------------------------------------------------------------------------------------------------------

# 3. Count Even numbers in the list

nums = [1, 4, 7, 10, 12]

count = 0
for num in nums:
    if num % 2 == 0:
        count += 1

print(f"Even numbers count is {count}")


#--------------------------------------------------------------------------------------------------------------------------------------

# 4. Remove Duplicates from the list 

nums = [1, 2, 2, 3, 4, 4, 5]

counter = 0

unique = []

# Here we take advantage of a unique python keyword: "Membership Keyword"
# we create a new list, and we check membership, if it doesnt exist, then its added first time
# if it exists already, then we skip the iteration and move to next 


for n in nums:
    if n not in unique:
        unique.append(n) 


print(unique)

# We iterate through the nums list, for every element, we check if it exists in "unique" list. If we are iterating through that element for the first time obviously that element wont exist inside the list. But if we are iterating through that element for the second time, "if not in unique" condition will fail, and hence the element wont be added the second time, thats how our resulting unique[] will contain only unique elements of nums[]


#-------------------------------------------------------------------------------------------------------------------------------------



# 5. Reverse a list - Method 1

nums = [12, 23, 5, 9 , 45, 10]

nums2 = nums[::-1]

print(f"The reversed list is {nums2}")




# 5. Reverse a list - Method 2

nums = [12, 23, 5, 9, 45, 10]

nums.reverse()

print(f"The reversed list using reverse() is {nums}")

#Remember: DO NOT confuse String functions with List functions. 
#Since strings are immutable, upon using string functions, changes are temporary.
# But in case of List functions, changes are permanent




# 5. Reverse a list - Method 3

nums = [12, 23, 5, 9, 45, 10]
rev_nums = []

for i in range(len(nums)-1, -1, -1):
    rev_nums.append(nums[i])

print(f"Reversed list using for loop {rev_nums}")


# we used:   for i in range(start idx,  end idx(not inclusive),   step)


#------------------------------------------------------------------------------------------------------------------------------------


   
    
    




    




