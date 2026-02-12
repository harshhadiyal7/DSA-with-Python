#Max consecutive ones.

'''
nums = [1,1,0,1,0,1,1,1,1,0,1,1]
we return any number how many time repeat.
ex: 1111}--->4
'''
#Optimal Solution
nums = [1,1,0,1,0,1,1,1,1,1,0,1,1]
count = 0
max_count = 0

for i in range (0, len(nums)):
    if nums [i] == 1:
        count += 1
    else:
        max_count = max(max_count, count)
        count=0
print (max(max_count, count))

'''
TC : O(N)
SC : O(1)
'''