from typing import List

def selection_sort(arr: List[int]) -> int:
    """
    https://www.hackerrank.com/challenges/lilys-homework/problem?isFullScreen=true

    Selection sort algorithm
    """
    swaps = 0
    for i in range(len(arr)):
        lowest_so_far = i
        for j in range(i, len(arr)):
            if arr[j] < arr[lowest_so_far]:
                lowest_so_far = j

        if lowest_so_far != i:
            arr[i], arr[lowest_so_far] = arr[lowest_so_far], arr[i]
            swaps += 1
    return swaps

def insertion_sort(arr: List[int]) -> int:
    """
    Implementation of the insertion sort.

    Returns the number of it takes to sort the array.
    """
    swaps = 0
    if len(arr) <= 1: return swaps

    for i in range(1, len(arr)):
        gap_idx = i
        value = arr[i]
        while gap_idx > 0:
            if arr[gap_idx - 1] > value:
                arr[gap_idx] = arr[gap_idx - 1]
                gap_idx -= 1
            else:
                arr[gap_idx] = value
                swaps += 1
                gap_idx = -1
        if gap_idx == 0:
            arr[0] = value
    
    return swaps

def bubble_sort(arr):
    """
    Implementation of the bubble sort (time complexity O^2).

    returns: the sorted array
    """
    swaps = 0
    unsorted_until_idx = len(arr)
    while unsorted_until_idx > 0:
        for i in range(1, unsorted_until_idx):
            if arr[i - 1] > arr[i]:
                # swap the values
                swaps += 1
                tmp = arr[i - 1]
                arr[i - 1] = arr[i]
                arr[i] = tmp
        unsorted_until_idx -= 1
    return swaps

def count_swaps(arr: List[int], reverse=False) -> int:
    indexes = [x[0] for x in sorted(enumerate(arr), key=lambda x: x[1], reverse=reverse)]
    visited = [False for _ in range(len(arr))]
    swaps = 0
    for i in range(len(arr)):
        if visited[i] or indexes[i] == i:
            continue
    
        j = i
        loops = 0
        while not visited[j]:
            visited[j] = True
            j = indexes[j]
            loops += 1
        
        if loops > 0:
            swaps += (loops - 1)
        
    return swaps

def homework(arr):
    return min(count_swaps(arr), count_swaps(arr, True))


if __name__ == '__main__':
    assert(homework([7, 15, 12, 3]) == 2)
    assert(homework([2, 5, 3, 1]) == 2)
    assert(homework([3, 4, 2, 5, 1]) == 2)