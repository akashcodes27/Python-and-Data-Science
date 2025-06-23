# Approach: 2 pointer

"""
In this approach, we use 2 pointers left and right
As we start iterating, we move the right pointer, 
and in every iteration we add element to CurSum   and    we compare if CurSum  = k
BELOW STEPS HAPPEN IN LOOP UNTIL THE END OF ARRAY
if CurSum < k, we continue moving right
if CurSum = k, we update compare MaxLength and update if bigger
if CurSum > k, we start moving left (subtracting elements from left)
"""


def longest_subarray_func(nums, k):
    left = 0
    right = 0
    CurSum = 0
    max_len = 0

    for right in range(len(nums)):

        CurSum += nums[right]

        while CurSum > k and left<=right:
            CurSum -= nums[left]

        if CurSum == k:
            max_len = max(max_len, right-left+1)


    return max_len







