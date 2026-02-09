# Move the 0 to the end of the list.

#Brute Force Solution
nums=[1,0,4,3,0,0,8,9,8,6]
n=len(nums)
temp=[]

for i in range(0,n):
    if nums[i]!=0:
        temp.append(nums[i])

nz=len(temp)
for i in range(0, nz):
    nums[i]=temp[i]
for i in range(nz, n):
    nums[i]=0
    
print(nums)

#Optimal Solution
nums = [1, 0, 4, 3, 0, 0, 8, 9, 8, 6]

if len(nums) == 1:
    print(nums) # Or return if inside a function

i = 0
while i < len(nums):
    if nums[i] == 0:
        break
    i += 1

if i == len(nums):
    print(nums) # Or return

j = i + 1

while j < len(nums):
    if nums[j] != 0:
        nums[i], nums[j] = nums[j], nums[i]
        i += 1
    j += 1 # This was likely the main issue!

print(nums)