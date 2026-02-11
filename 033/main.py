#Reture missing number.
'''
nums = [9,6,4,2,3,5,7,0,1]
we return missing number 8.
'''


#Brute Force Solution
nums = [9,6,4,3,5,7,0,1]
n=len(nums)
for i in range (0, n+1):
    if i not in nums:
        print(i)

'''
TC: O(N^2)
SC: O(1)
'''

#Better Solution
nums = [9,6,4,3,5,7,0,1]   

n = len(nums)
freq = {}
for i in range(1, n+1):
    freq[i] = 0

for num in nums:
    if num in freq:
        freq[num] += 1

for k, v in freq.items():
    if v == 0:
        print(k)

'''
Tc: O(N)
Sc: O(N)
'''