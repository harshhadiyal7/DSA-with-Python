# Remove duplicate eliment for the list. 

nums = [1,1,1,2,3,4,4,7,9,9,9,10]

#Method 1: Brute Force Approach

n=len(nums)
freq_map={}
for i in range(0,n):
    freq_map[nums[i]]=0
j=0
for k in freq_map.keys():
    nums[j]=k
    j+=1
print(nums[:j])  # Output the list without duplicates

'''
Tc: O(n)    Sc: O(n)
'''

#Method 2:  Optimal Approach

n = len(nums)
if n == 0:
    print([])
    exit()

i = 0
for j in range(1, n):
    if nums[j] != nums[i]:
        i += 1
        nums[i] = nums[j]

print(nums[:i+1])
