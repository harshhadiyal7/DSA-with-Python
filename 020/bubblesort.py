# Bubble sort implementation in Python.

'''
Concept: Bubble sort is a simple sorting algorithm that repeatedly steps through the list, {compares adjacent elements and swaps them} 
if they are in the wrong order.
The pass through the list is repeated until the list is sorted.
'''


nums = [5,1,6,8,2,4,9]

n = len(nums)

for i in range (n-2, -1, -1):
    for j in range (0, i+1):
        if nums[j] > nums[j+1]:
            # swap
            nums[j], nums[j+1] = nums[j+1], nums[j]
print(nums)

'''
output:
[1, 2, 4, 5, 6, 8, 9]

Tc: O(N(N+1))/2 = O(n^2)
Sc: O(1)
This is for Average and Worst case.

For BEST case Tc: O(N)
              Sc: O(1)

'''