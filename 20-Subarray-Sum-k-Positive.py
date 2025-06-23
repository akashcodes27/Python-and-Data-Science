
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




