#Reverse array using recursion.

'''
Concept: To reverse an array using recursion, we can swap the first and last elements and then recursively call the function 
for the sub-array excluding these two elements until the base case is reached.
'''
nums=[2,4,1,7,6,3,8,9,5]

def func(nums, left, right):
    if left >= right:
        return
    nums[left], nums[right] = nums[right], nums[left]
    func(nums, left + 1, right - 1)
    return nums
print(func(nums, 0, len(nums) - 1))

    
