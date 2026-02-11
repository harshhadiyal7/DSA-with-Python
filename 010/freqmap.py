# Stored frequency map in dictionary.
'''
nums = [5,6,7,7,1,9,111,1,5,1,1]

eg: 
    1: 4
    5: 2
    7: 2
    9: 1
    111: 1
'''
# Method 1
nums = [5,6,7,7,1,9,111,1,5,1,1,1,1]
freq_map = {}
for i in range(0, len(nums)):
    
    if nums[i] in freq_map:
        freq_map[nums[i]] += 1
    else:
        freq_map[nums[i]] = 1
print(freq_map)
# Time Complexity: O(n) Space Complexity: O(n)

# Method 2

'''
nums = [5,6,7,7,1,9,111,1,5,1,1]

eg: 
    1: 4
    5: 2
    7: 2
    9: 1
    111: 1
    
hash_map[nums[3]] = hash_map.get(nums[3], 0) + 1
    Here, nums[3] = 7
    If 7 is already present in hash_map, then get its value and add 1 to it.
    If 7 is not present in hash_map, then get returns the default value 0, and we add 1 to it.
'''
nums = [5,6,7,7,1,9,111,1,5,1,1,1,1]
hash_map = {}
n=len(nums)
for i in range(0, n):
    hash_map[nums[i]] = hash_map.get(nums[i], 0) + 1
print(hash_map)
