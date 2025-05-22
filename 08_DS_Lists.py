# Data Structure: Lists


fruits = ["apples", 'bananas', "grapes", "peaches", "oranges", "kiwi"]



#List Operations

#Accessing Elements
print(fruits[0])
print(fruits[3])
print(fruits[4])
print(fruits[-1])    # returns the last element of list



#Modifying Elements
fruits[0] = "APPLES" 
fruits[3] = "PEACHES"



#Adding Elements
fruits.append("lemon")     # Adds new element at last index 
fruits.insert(3, "Tomato")  # Adds new element at specified index
print(fruits)





#Removing Elements
fruits.remove("grapes")     # Removes the specified element
fruits.pop()                # Removes the last element from list 
del fruits[0]               # Removes element with specified index 

print(fruits)



#Looping through a list
for fruit in fruits:
    print(fruit) 



#Checking Membership
if "mango" in fruits:
    print("Yes mango exits")
else:
    print("No Mango does not exist")


if "kiwi" in fruits:
    print("Yes, kiwi exists")
else:
    print("No, kiwi does not exist")



#Checking length of lists:
print(len(fruits))