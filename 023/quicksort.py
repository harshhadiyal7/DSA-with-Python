# Quick sort alogorithm implementation in Python.

'''
nums = [4,1,7,6,3,2,8]

1. Pick a pivot
- it can be the first element
- it can be the last element
- it can be a random element
- it can be the median element
2. Put pivot at its correct position/index
'''

nums = [4,1,7,6,3,2,8]
def partition(nums, low, high):
    pivot = nums[low]
    i = low
    j = high
    while i < j:
        while nums[i] <= pivot and i <= high - 1:
            i += 1
        while nums[j] > pivot and j >= low:
            j -= 1
        if i < j:
            nums[i], nums[j] = nums[j], nums[i]
    nums[low], nums[j] = nums[j], nums[low]
    return j

def quick_sort(nums, low, high):
    if low < high:
        pivot_index = partition(nums, low, high)
        quick_sort(nums, low, pivot_index - 1)
        quick_sort(nums, pivot_index + 1, high)
    return nums

sorted_nums = quick_sort(nums, 0, len(nums) - 1)    
print(sorted_nums)

'''
output: [1, 2, 3, 4, 6, 7, 8]
Time Complexity: O(n log n) on average, O(n^2) in the worst case
Space Complexity: O(log n) due to recursive stack space 
'''