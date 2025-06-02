
"""
Input:  s = "abcabcbb"
Output: 3
Explanation: The longest substring is "abc"

"""


def longest_nonrepeating_substring(str):

    l = 0
    unique_dict = {}
    max_len = 0


    for r in range(len(str)):

        if str[r] in unique_dict and unique_dict[str[r]] >= 1:
            l = unique_dict[str[l]] + 1   #updates "l" to exclude repeated character

        unique_dict[str[r]] = r 
        max_len = max(max_len, r-l+1)
    
    return max_len















"""
Input:  s = "abcbcbb"
Output: 3
Explanation: The longest substring is "abc"



Technique:
We use a dictionary to keep track of unique characters. 
We use a sliding window two pointers approach
If we encounter a character once, we store it in dictionary
If we encounter it again, we move p1 to one step beyond first occurance of duplicate character
And p2 to one step beyond p1
and then we continue

"""