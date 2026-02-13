# Find the maximum sub array.

'''
Problem:
Given a list of numbers (positive + negative), find the continuous subarray that has the maximum sum.

Example:
nums = [-2,1,-3,4,-1,2,1,-5,4]
Best subarray = [4, -1, 2, 1]
Maximum sum = 6

'''
#Brute Force solution
nums = [-2,1,-3,4,-1,2,1,-5,4]
n=len(nums)
maxi=float("-inf")
for i in range (0, n):
    total=0
    for j in range(i,n):
        total = total + nums[j]
        maxi = max(maxi, total)
print(maxi)
