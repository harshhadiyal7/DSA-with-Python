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
