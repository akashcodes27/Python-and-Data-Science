
# How to take input in python:  input()
# Note: input() always returns "string" not "int"


#Taking string input
name = input("Enter Your Name")
print("Hello"+ name)


#Taking integer input
age = int(input("Enter your age"))
print(f"you will be {age + 1} years old next year")


#"f" is used to embbed variables in a string in print statement. for eg: {name1} and {uni}
name1 = "akash"
uni = "University Of Windsor"
print(f"My name is {name1} and I study in {uni}")
