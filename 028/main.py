# Right Rotate an Array by One Place.

'''
(frequency map)
'''
nums = [1,1,1,2,3,4,4,7,9,9,9,10]
#Brute Force Approach:
n=len(nums)
freq_map={}
for i in range(0,n):
    freq_map[nums[i]]=0
j=0
for k in freq_map:
    nums[j]=k
    j+=1
print(nums[:j])
