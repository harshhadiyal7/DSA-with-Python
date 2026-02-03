#Find Largest element in an Array.

'''
nums = [10, 24, 56, 78, 34, 89, 12]
take i and assume it is largest
and compare with each element in the array
if any element is greater than i
then assign that element to i
finally i will have the largest element.
'''
nums = [10, 24, 56, -78, 34, 89, 12]

#Methond 1:
largest = nums[0]  # Assume the first element is the largest
n=len(nums)
for i in range(0, n):
    if nums[i] > largest:
        largest = nums[i]
print(largest)

#Method 2:
largest= nums[0]
n=len(nums)
for i in range(0, n):
        largest=max(largest, nums[i])
print(largest)      

#Method 3:
largest = float('-inf')  # Initialize to the smallest possible value
n=len(nums)
for i in range(0, n):
    largest=max(largest, nums[i])   
print(largest)