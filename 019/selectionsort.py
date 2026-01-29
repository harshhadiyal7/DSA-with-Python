# Selection Sort Implementation.
nums = [1,7,8,4,5,6,9,2]
def selection_sort(nums):
    n=len(nums)
    for i in range(0, n):
        min_ind=i
        for j in range(i+1, n):
            if nums[j]<nums[min_ind]:
                min_ind=j
        nums[i], nums[min_ind]=nums[min_ind], nums[i]
selection_sort(nums)
print(nums)

'''
TC: O(n^2)
SC: O(1)
'''