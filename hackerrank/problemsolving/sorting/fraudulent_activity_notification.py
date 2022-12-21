#!/bin/python3

import math
import os
import random
import re
import sys

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

def fraudulent_notifications_heap(trailing_days, expenditures):
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

    
def activityNotifications(expenditures, d):
    import queue
    median = Median()
    fifo = queue.SimpleQueue()
    notification_count = 0

    for i in range(len(expenditures)):
        if i < d:
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

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    d = int(first_multiple_input[1])

    expenditure = list(map(int, input().rstrip().split()))

    result = activityNotifications(expenditure, d)

    fptr.write(str(result) + '\n')

    fptr.close()
