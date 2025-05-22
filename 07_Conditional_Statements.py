# Example 1:   if-elif-else

age = 23


if age>18 and age<30:
    print("You are a young adult")

elif age>30 and age<60:
    print("You are an adult")

else:
    print("You are either a child or an old man")






# Example 2     if-elif-else

marks = 95

if marks<=30:
    print("You have failed your exams")

elif marks<= 60 and marks>30:
    print("You have passed satisfactorily")

elif marks<=90 and marks>60:
    print("You have scored Good Marks")

else:
    print("You are one of the toppers")



# for loop 
# prints numbers from to 1 to 5: 1,2,3,4,5 
for i in range(1,6):
    print(i)




# while loop
var = 1
while(var <= 10):
    print(var)
    var+=1





# Loop Control Statements 
# Break, Continue


# skips one iteration at i==4
for i in range(1,8):
    if i == 4:
        continue      
    print(i)



# breaks out of loop after i==5 
for i in range(1,10):
    if i == 5:
        break
    print(i)