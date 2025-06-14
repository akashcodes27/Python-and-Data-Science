# main logic:
# as we iterate through the list, we store elements in the dictionary,
# and for every iteration, we check if difference of target and current number exists in dictionary. 
# for some initial iterations, obviously the differne wont exist in the dictionary. But as we continue to iterate through the list, we begin to observe that the difference does exist in dict, and once we find the first occurance of such number, we return the index of current number, and index of number found in dictionary

nums = [2, 5, 7, 16, 9, 12, 8, 3]
target = 12

seen = {}

for idx, num in enumerate(nums):
    diff = target - num
    if diff in seen:
        print( [idx, seen[diff]])
    
    seen.update({num: idx})
    
# print("Nothing Found")