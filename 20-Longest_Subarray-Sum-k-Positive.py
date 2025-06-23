
def longest_subarray_sum_k(nums, k):
    prefix_sum = 0
    max_len = 0
    seen = {}  # prefix_sum: index

    for i, num in enumerate(nums):
        prefix_sum += num

        if prefix_sum == k:
            max_len = i + 1  # from index 0 to i

        # Check if there is a previous prefix_sum that makes current sum - k
        if (prefix_sum - k) in seen:
            length = i - seen[prefix_sum - k]
            max_len = max(max_len, length)

        # Store the first occurrence of this prefix_sum
        if prefix_sum not in seen:
            seen[prefix_sum] = i

    return max_len



# Approach using hashmap:


"""
In this approach:
We use hashmap to store prefix. 
So as we start iterating through the array, we start taking sum , and then we compare sum with "k" in each iteration. 
Whenever sum !=k, we try to find and get rid of a prefix subarray so that we can obtain a subarray with sum = k

EASY WAY to UNDERSTAND: CurSum - k gives us a value whose subarray if we subtract from CurSum we get k. we check if CurSum - k exists in hashmap, if it does, we have successfully found a subarray in hashmap which if we subtract from CurSum, we get k
Everytime we find the subarray whose sum is k, we find its length, compare it with maxlength, and then if its bigger, we update the maxlength. 

"""


