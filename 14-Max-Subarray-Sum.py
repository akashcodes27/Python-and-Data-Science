
# Given an array and a number k, find the maximum sum of any subarray of size k 



def func1(arr, k):

    cur_sum = sum(arr[:k])
    max_sum = cur_sum

    l = 0  #(points to first position of window)
    r = k  #(points to position 1 more than last element of window)

    for i in range(r, len(arr)):

        cur_sum = cur_sum - arr[l] + arr[r]

        max_sum = max(max_sum, cur_sum)

        
        l+=1
        r+=1

    
    return max_sum 



print(func1([2, 1, 5, 7, 3, 2], 3))

        
























