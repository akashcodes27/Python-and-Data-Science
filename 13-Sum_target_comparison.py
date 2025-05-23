
# Find two elements such that their sum is equal to target



def  sum_of_target(arr, target):
    left = 0
    right = len(arr)-1

    while left < right:
 
        cur_sum = arr[left] + arr[right]

        if cur_sum == target:
            return True 
        
        elif cur_sum < target:
            left +=1
        
        else:
            right-= 1

    
    return False


print(sum_of_target([1,12,20,33,38,40,45], 81))

     












