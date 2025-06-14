#Now we shall solve Reverse String using stack 

str = ["h", "e", "l", "l", "o"]

#in python, stacks are implemented using python lists
stack1 = []
l = 0

for ele in str:
    stack1.append(ele)

while stack1:
    str[l] = stack1.pop()
    l += 1

print(str)








