from curses import window
from queue import SimpleQueue
from typing import List
from unittest import expectedFailure
import random

# https://www.hackerrank.com/challenges/fraudulent-activity-notifications/problem
# fails due to timeout

def fraudulent_notifications(trailing_days: int, expenditure: List[int]) -> int:
    notification_count = 0
    for i in range(len(expenditure)):
        if i < trailing_days:
            continue
        
        median_value = quickselect_median(expenditure[i - trailing_days:i])

        if expenditure[i] >= 2 * median_value:
            notification_count += 1
    return notification_count


def fraudulent_notifications_v3(trailing_days, expenditures):
    import queue
    window = []
    fifo = queue.SimpleQueue()
    notification_count = 0

    for i in range(len(expenditures)):
        if i < trailing_days:
            fifo.put(expenditures[i])
            window.append(expenditures[i])
            continue

        if i == trailing_days:
            window.sort()
        
        median_value = median(window)
        if expenditures[i] >= 2 * median_value:
            notification_count += 1
        
        to_remove = fifo.get()
        to_remove_idx = binary_search(window, to_remove)
        window[to_remove_idx] = expenditures[i]
        partition_v3(window, to_remove_idx)
        #window.sort()

    return notification_count

def partition_v3(arr, pivot_idx):
        pivot = arr[pivot_idx]
        store_idx = 0
        last_idx = len(arr) - 1
        arr[last_idx], arr[pivot_idx] = arr[pivot_idx], arr[last_idx]

        for i in range(len(arr)):
            if arr[i] < pivot:
                arr[store_idx], arr[i] = arr[i], arr[store_idx]
                store_idx += 1
        
        arr[store_idx], arr[last_idx] = arr[last_idx], arr[store_idx]

def binary_search(arr, x):
        low = 0
        high = len(arr) - 1
        mid = 0
    
        while low <= high:
    
            mid = (high + low) // 2
    
            # If x is greater, ignore left half
            if arr[mid] < x:
                low = mid + 1
    
            # If x is smaller, ignore right half
            elif arr[mid] > x:
                high = mid - 1
    
            # means x is present at mid
            else:
                return mid
    
        # If we reach here, then the element was not present
        return -1
    

def median(sorted_expenditure: List[int]) -> float:
    length = len(sorted_expenditure)
    half = length // 2
    if length == 0:
        return 0
    if length % 2 == 0:
        return (sorted_expenditure[half - 1] + sorted_expenditure[half]) / 2
    return sorted_expenditure[half]


def quickselect_median(expenditure):

    def partition(arr, left_idx, right_idx, until_idx):
        pivot_idx = random.randint(left_idx, right_idx)
        pivot = arr[pivot_idx]
        arr[right_idx], arr[pivot_idx] = arr[pivot_idx], arr[right_idx]
        
        store_idx = left_idx
        for i in range(left_idx, right_idx):
            if arr[i] < pivot:
                arr[store_idx], arr[i] = arr[i], arr[store_idx]
                store_idx += 1
        
        arr[store_idx], arr[right_idx] = arr[right_idx], arr[store_idx]

        if store_idx == until_idx: 
            return arr[store_idx]
        elif store_idx > until_idx:
            return partition(arr, left_idx, store_idx - 1, until_idx)
        else:
            return partition(arr, store_idx + 1, right_idx, until_idx)

    length = len(expenditure)
    middle = length // 2

    if length == 1:
        return expenditure[0]
    elif length % 2 == 0:
        return (partition(expenditure, 0, length - 1, middle - 1) + \
            partition(expenditure, middle, length - 1, middle)) / 2
    else:
        return partition(expenditure, 0, length - 1, middle)
    
import heapq
from collections import deque

class Median:
    def __init__(self):
        self.left = [] # max heap
        self.right = [] # min heap

    def rebalance(self):
        if len(self.right) > len(self.left):
            heapq.heappush(self.left, heapq.heappop(self.right) * -1)
        if len(self.right) < len(self.left):
            heapq.heappush(self.right, heapq.heappop(self.left) * -1)
    
    def push(self, el):
        if len(self.left) == 0:
            heapq.heappush(self.left, el * -1)
        elif el > self.left[0] * -1:
            heapq.heappush(self.right, el)
        else:
            heapq.heappush(self.left, el * -1)
        
        self.rebalance()
    
    def remove(self, el):
        if el > self.left[0] * -1:
            idx = self.right.index(el)
            del self.right[idx]
            heapq.heapify(self.right)
        else:
            idx = self.left.index(el * -1)
            del self.left[idx]
            heapq.heapify(self.left)
        
        self.rebalance()

    def median(self):
        size = len(self.left) + len(self.right)
        if size == 0:
            return None
        elif size % 2 != 0:
            return self.right[0]
        else: 
            return (self.left[0] * -1 + self.right[0]) / 2

def heap_median(expenditure):
    median = Median()
    for i in expenditure:
        median.push(i)
    return median.median()

def fraudulent_notifications_heap(trailing_days: int, expenditure: List[int]) -> int:
    notification_count = 0
    median = Median()
    for i in range(len(expenditure)):
        if i < trailing_days:
            continue
        
        median_value = heap_median(expenditure[i - trailing_days:i])

        if expenditure[i] >= 2 * median_value:
            notification_count += 1
    return notification_count


def fraudulent_notifications_heap_v2(trailing_days: int, expenditures: List[int]) -> int:
    import queue
    median = Median()
    fifo = queue.SimpleQueue()
    notification_count = 0

    for i in range(len(expenditures)):
        if i < trailing_days:
            fifo.put(expenditures[i])
            median.push(expenditures[i])
            continue
        
        median_value = median.median()
        if expenditures[i] >= 2 * median_value:
            notification_count += 1
        
        to_remove = fifo.get()
        median.remove(to_remove)

        fifo.put(expenditures[i])
        median.push(expenditures[i])

    return notification_count

class SlidingMedianCountingSort():

    def __init__(self, window_size, max_value):
        self._frequencies = [0 for i in range(max_value + 1)]
        self._count = 0
        self._window_size = window_size

    def push(self, value):
        self._frequencies[value] += 1
        self._count += 1
    
    def remove(self, value):
        self._frequencies[value] -= 1
    
    def median(self):
        acc = 0
        if self._window_size % 2 != 0:
            for v, f in enumerate(self._frequencies):
                acc += f
                if acc > self._window_size // 2:
                    return v
        else:
            a = 0
            b = 0
            for v, f in enumerate(self._frequencies):
                acc += f
                if acc >= self._window_size // 2 and a == 0:
                    a = v
                if acc >= (self._window_size // 2) + 1 and b == 0:
                    b = v
                if a != 0 and b != 0:
                    break
            return (a + b) / 2
    
    def sorted(self):
        sorted = []
        for i in range(0, len(self._frequencies)):
            if self._frequencies[i] != 0:
                sorted[len(sorted):] = [i for j in range(0, self._frequencies[i])]

        return sorted

def fraudulent_notifications_counting_sort(trailing_days, expenditures):
    median = SlidingMedianCountingSort(trailing_days, 200)
    notification_count = 0

    for i in range(len(expenditures)):
        if i < trailing_days:
            median.push(expenditures[i])
            continue
        median_value = median.median()
        if expenditures[i] >= 2 * median_value:
            notification_count += 1

        median.remove(expenditures[i - trailing_days])
        median.push(expenditures[i])

    return notification_count

if __name__ == "__main__":
    import time
    import random

    # expenditures = [random.randint(0, 200) for i in range(2 * 10**5 + 1)]
    
    # t1 = time.time()
    # res = fraudulent_notifications_counting_sort(10**4, expenditures)
    # t2 = time.time()
    # print(f"fraudulent_notifications_counting_sort : {t2 - t1} seconds - {res}")

    # t1 = time.time()
    # res = fraudulent_notifications_heap(10**3, expenditures)
    # t2 = time.time()
    # print(f"fraudulent_notifications_heap : {t2 - t1} seconds {res}")

    # t1 = time.time()
    # res = fraudulent_notifications(10**3, expenditures)
    # t2 = time.time()
    # print(f"fraudulent_notifications : {t2 - t1} seconds - {res}")

    # t1 = time.time()
    # res = fraudulent_notifications_heap_v2(10**4, expenditures)
    # t2 = time.time()
    # print(f"fraudulent_notifications_heap_v2 : {t2 - t1} seconds - {res}")

    # import timeit
    # print(timeit.timeit(lambda: fraudulent_notifications_counting_sort(10**4, expenditures), number=1))

    import matplotlib as mpl
    import matplotlib.pyplot as plt
    import timeit

    expediture_sizes = [j*10**i for i in range(1, 6) for j in range(1, 10)]
    
    times_a = []
    times_b = []
    linear = []
    for size in expediture_sizes:
        expenditures = [random.randint(0, 200) for x in range(size)]
        window_size = len(expenditures) // 3
        times_a.append(timeit.timeit(lambda: fraudulent_notifications_counting_sort(window_size, expenditures), number=1))
        times_b.append(timeit.timeit(lambda: fraudulent_notifications_heap_v2(window_size, expenditures), number=1))
        linear.append(size)

    fig, ax = plt.subplots()  # Create a figure containing a single axes.
    ax.plot(expediture_sizes, times_a)
    ax.plot(expediture_sizes, times_b)  # Plot some data on the axes.

    fig.savefig("test.png")