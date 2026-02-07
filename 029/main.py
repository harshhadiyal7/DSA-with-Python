#Right Rotate an Array by K Places 

#Brute Force Approach
nums = [3,9,5,6,7,2]
k = 3
n=len(nums)
rotations = k % n
for i in range(0, rotations):
    e =nums.pop()
    nums.insert(0,e)
print(nums)
'''
Tc: O(n*k) where n is the number of elements in the array and k is the number of rotations
Sc: O(1) as we are not using any extra space for another array, we
'''
#Better Approach
nums = [3,9,5,6,7,2,10,9]
k=5
n=len(nums)
k = n%k
nums[:] = nums[n-k:]+nums[:n-k]
print(nums)
'''
Tc: O(n) where n is the number of elements in the array
Sc: O(n) as we are creating a new array to store the rotated elements
'''

#Optimal Approach
nums = [3,9,5,6,7,2,10,9]

def reverse(nums, start, end):
    while start < end:
        nums[start], nums[end] = nums[end], nums[start]
        start += 1
        end -= 1
k=5
n=len(nums)
reverse(nums, 0, n-1)
reverse(nums, 0, k-1)
reverse(nums, k, n-1)
print(nums) 
'''
Tc: O(n) where n is the number of elements in the array
Sc: O(1) as we are not using any extra space for another array, we'''