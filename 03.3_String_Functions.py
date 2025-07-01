
# String Functions in Python 


str1 = "University Of Windsor is the best"
str2 = "I LIVE IN WINDSOR ONTARIO"





# lower(), upper()
print(str1.upper())    # Convert to Uppercase
print(str2.lower())    # Convert to lowercase





# strip(), lstrip(),  rstrip()
str3 = "    Lets go the gym today evening    "
print(str3.strip())   # Removes of empty spaces 
print(str3.lstrip())  # Removes left empty spaces
print(str3.rstrip())  # Removes right empty spaces 







# split()
arr1 = str1.split(" ")    # Converts string to list(array), every "space" creates separate element in list
print(arr1)

string1 = "Canada,is very,beautiful, it has, many, cities"
arr2 = string1.split(",")  # Converts string to list, every "comma" creates separate element in list 
print(arr2)





# find(), index()
print(string1.find("ana"))    # returns index of first character of substring
print(string1.index("ana"))   # returns index of first character of substring 





# startswith(), endswith() 
# Compares whatever we have passed through the () with the start of the string (Not just first characters)
string1 = "Canada ,is very,beautiful, it has, many, cities"
print(string1.startswith("Canada"))    # returns True
print(string1.startswith("Canady"))    # returns false

print(string1.endswith(", cities"))   # returns True
print(string1.endswith(",cities"))   # returns False





# count() : Counts the number of occurances of a character or string
str1 = "Canada, United States Of America, India, Asia, Country, City, ia, ia, ia"
print(str1.count("a"))
print(str1.count('i'))
print(str1.count("C"))
print(str1.count("ia"))




# isalpha(), isdigit(), isalnum() 
print("Hello".isalpha())              #returns True
print("Hello12345".isalnum())         #returns True
print("123456".isdigit())             #returns True 





# replace()
str1 = "Canada is very beautiful Country"
str2 = str1.replace("Canada", "India")        
print(str2)

#strings are immutable, upon using "replace()", str1 doesnt change permanently, it only changes temporarily, hence to save the change we use "str2



# To generate "Reversed" strings 
str1 = "madam"
str2 = "Canada"
print(str1[::-1])     #generates "madam"
print(str2[::-1])     #generates "adanaC"