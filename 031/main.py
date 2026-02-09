#Impliment linear search.

def find_target(nums, target):
    n = len(nums)
    for i in range(0, n):
        if nums[i] == target:
            return i # Success! Exit and give the index
            
    return -1 # We finished the loop and found nothing

# Testing it out
nums = [5, 3, 9, 8, 1, 6, 4, -10, -100]
print(find_target(nums, 4))