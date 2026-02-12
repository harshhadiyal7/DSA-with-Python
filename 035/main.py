# Two sum.
'''
nums = [5,9,1,2,4,15,6,3]
return index of target sum 2 numbers.
for ex: target=13  and 9 and 4 are numbers and we resturn index of 9 and 4. it means [1,4].
'''
#Brute force solution.
nums = [5,9,1,2,4,15,6,3]
target=13
n=len(nums)
for i in range (0, n-1):
    for j in range(i+1,n):
        if nums[i]+nums[j] == target:
            print(i,j)