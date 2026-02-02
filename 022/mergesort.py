# Merge Sort Implementation in Python

'''
Concept: Merge sort is a divide-and-conquer algorithm that divides the input array into two halves,
recursively sorts each half, and then merges the two sorted halves back together.
'''

from turtle import left, right
arr = [38, 27, 43, 3, 9, 82, 10]

def merge_sort(arr):
    if len(arr) <= 1:# base case
        return arr
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]
    
    left = merge_sort(left)# recursive calls
    right = merge_sort(right)

    return merge(left, right) # merge step

def merge(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])# add remaining elements
    result.extend(right[j:])
    return result
print("Unsorted Array:", arr)
print("Sorted Array:", merge_sort(arr))

'''
output:
Unsorted Array: [38, 27, 43, 3, 9, 82, 10]
Sorted Array: [3, 9, 10, 27, 38, 43, 82]
Time Complexity: O(n log n)
Space Complexity: O(n)
'''
