from hypothesis import given, strategies as st
from problemsolving.sorting.fraudulent_activity_notification import median, quickselect_median, heap_median, fraudulent_notifications, fraudulent_notifications_heap
import statistics

@given(arr=st.lists(st.integers(), min_size=1))
def test_median(arr):
    assert statistics.median(arr) == median(arr)

@given(arr=st.lists(st.integers(min_value=0), min_size=100, max_size=200))
def test_quickselect_median(arr):
    assert statistics.median(arr) == quickselect_median(arr)
 
@given(arr=st.lists(st.integers(min_value=0), min_size=100, max_size=200))
def test_heap_median(arr):
    assert statistics.median(arr) == heap_median(arr)

def test_fraudulent_notifications():
    assert 2 == fraudulent_notifications(5, [2, 3, 4, 2, 3, 6, 8, 4, 5])
    assert 1 == fraudulent_notifications(3, [10, 20, 30, 40, 50])

def test_fraudulent_notifications_heap():
    assert 2 == fraudulent_notifications_heap(5, [2, 3, 4, 2, 3, 6, 8, 4, 5])
    assert 1 == fraudulent_notifications_heap(3, [10, 20, 30, 40, 50])
