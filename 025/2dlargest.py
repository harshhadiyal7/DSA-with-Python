# Find Second Largest element in an Array.

#Method 1:Brute Force
nums = [10, 24, 56, -78, 34, 89, 12]
nums.sort()
n=len(nums)
print(nums[n-2])

'''
Tc: O(nlogn) due to sorting
Sc: O(1)
'''
#Method 2:Better Approach
nums = [10, 24, 56, -78, 34, 89, 12]

largest = float('-inf')
second_largest = float('-inf')

n = len(nums)

# Find largest
for i in range(n):
    largest = max(largest, nums[i])

# Find second largest
for i in range(n):
    if nums[i] > second_largest and nums[i] != largest:
        second_largest = nums[i]

print(second_largest)
'''
Tc: O(2n) => O(n)
Sc: O(1)'''


#Method 3:Optimal Approach
nums = [10, 24, 56, -78, 34, 89 , 12]
largest = float('-inf')  # Initialize to the smallest possible value
second_largest = float('-inf')  # Initialize to the smallest possible value
for i in range(0,n):
    if nums[i]>largest:
        second_largest=largest
        largest=nums[i]
    elif nums[i]>second_largest and nums[i]!=largest:
        second_largest=nums[i]
print(second_largest)
'''
Tc: O(n)
Sc: O(1)'''