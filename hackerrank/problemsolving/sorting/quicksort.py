from turtle import left
from typing import List

#https://www.hackerrank.com/challenges/quicksort1

def partition(arr, left_idx, right_idx):
    pivot = arr[left_idx]
    arr[right_idx], arr[left_idx] = arr[left_idx], arr[right_idx]
    
    store_idx = left_idx
    for i in range(left_idx, right_idx):
        if arr[i] < pivot:
            arr[store_idx], arr[i] = arr[i], arr[store_idx]
            store_idx += 1
    
    arr[store_idx], arr[right_idx] = arr[right_idx], arr[store_idx]
    return arr

def quicksort(arr: List[int]) -> List[int]:
    
    def _quicksort(arr, left_idx, right_idx): 
        if (right_idx - left_idx) < 1: return arr
        
        pivot = arr[left_idx]
        arr[right_idx], arr[left_idx] = arr[left_idx], arr[right_idx]
        
        store_idx = left_idx
        for i in range(left_idx, right_idx):
            if arr[i] < pivot:
                arr[store_idx], arr[i] = arr[i], arr[store_idx]
                store_idx += 1
        
        arr[store_idx], arr[right_idx] = arr[right_idx], arr[store_idx]

        _quicksort(arr, left_idx, store_idx - 1)
        _quicksort(arr, store_idx + 1, right_idx)

        return arr
    
    return _quicksort(arr, 0, len(arr) - 1)


if __name__ == "__main__":
    print(quicksort([4, 5, 3, 7, 2]))