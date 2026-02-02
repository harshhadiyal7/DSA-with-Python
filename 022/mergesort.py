# Merge Sort Implementation in Python

'''
Concept: Merge sort is a divide-and-conquer algorithm that divides the input array into two halves,
recursively sorts each half, and then merges the two sorted halves back together.
'''

from turtle import left, right

arr = [38, 27, 43, 3, 9, 82, 10]

def merge_sort(arr):
    # base case
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]

    # recursive calls
    left = merge_sort(left)
    right = merge_sort(right)

    # merge step
    return merge(left, right)


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

    # add remaining elements
    result.extend(left[i:])
    result.extend(right[j:])

    return result


arr = [38, 27, 43, 3, 9, 82, 10]
print("Unsorted Array:", arr)
print("Sorted Array:", merge_sort(arr))
