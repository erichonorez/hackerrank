from typing import Any, List

# https://www.hackerrank.com/challenges/runningtime/problem

def insertion_sort(arr: List[int]) -> List[int]:
    """
    Implementation of the insertion sort.

    Returns the sorted array
    """
    if len(arr) <= 1: return arr

    for i in range(1, len(arr)):
        gap_idx = i
        value = arr[i]
        while gap_idx > 0:
            if arr[gap_idx - 1] > value:
                arr[gap_idx] = arr[gap_idx - 1]
                gap_idx -= 1
            else:
                arr[gap_idx] = value
                gap_idx = -1
        if gap_idx == 0:
            arr[0] = value
    
    return arr

def insertion_sort_shifts(arr: List[int]) -> int:
    """
    Implementation of the insertion sort.

    Returns the number of it takes to sort the array.
    """
    shifts = 0
    if len(arr) <= 1: return shifts

    for i in range(1, len(arr)):
        gap_idx = i
        value = arr[i]
        while gap_idx > 0:
            if arr[gap_idx - 1] > value:
                arr[gap_idx] = arr[gap_idx - 1]
                shifts += 1
                gap_idx -= 1
            else:
                arr[gap_idx] = value
                gap_idx = -1
        if gap_idx == 0:
            arr[0] = value
    
    return shifts
    
