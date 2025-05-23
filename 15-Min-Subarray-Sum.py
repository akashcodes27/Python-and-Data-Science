def min_subarray_sum(arr, k):

    p1 = 0
    p2 = k 

    cur_sum = sum(arr[:k])
    min_sum = cur_sum

    for i in range(k, len(arr)):

        cur_sum = cur_sum - arr[p1] + arr[p2]
        min_sum = min(min_sum, cur_sum)
        p1+=1
        p2+=1

    
    return min_sum

   

print(min_subarray_sum([9, 4, 1, 8, 3, 5, 2, 7], 4))



 # so we use the two pointers sliding window approach, we consider a window of subarray of size k
    # we find sum of initial subarray. 
    # Then for subsequent subarrays, we simple remove the first element and add a new element
    #so we define two pointers p1 and p2
    # p1 will point to index of element that needs to be removed
    # p2 will point to index of element that needs to be added to window

    #we define a for loop who's last limit is last element of array


