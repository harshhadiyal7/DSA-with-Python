# Insertionsort implementation in Python.
'''
Concept: Insertion sort is a simple sorting algorithm that builds the final sorted array one item at a time.
It is much less efficient on large lists than more advanced algorithms such as quicksort, heapsort, or merge sort.
(key idea): The array is virtually split into a sorted and an unsorted part.
'''

nums = [3,5,6,4,8,9,10,7,1]

n = len(nums)
for i in range (1, n):
    key = nums[i]
    j=i-1
    
    while j>=0 and nums[j]>key:
        nums[j+1] = nums[j]
        j -= 1
        
    nums[j+1] = key
print("Sorted array is:", nums)

'''
output:
Sorted array is: [1, 3, 4, 5, 6, 7, 8, 9, 10]

Time Complexity: O(n^2)
Space Complexity: O(1)
'''