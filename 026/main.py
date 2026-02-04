#check array is sorted or not.

nums = [1, 2, 3, 4, 5]
n = len(nums)
for i in range(0, n-1):
    if nums[i] > nums[i+1]:
        print("Array is not sorted")
        break
else:
    print("Array is sorted")

'''
TC: O(n)
SC: O(1)
'''