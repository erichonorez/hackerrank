from hypothesis import given, strategies as st
from hackerrank.problemsolving.sorting.runningtime import insertion_sort, insertion_sort_shifts


@given(arr=st.lists(st.integers(), max_size=100))
def test_insertion_sort(arr):
    assert insertion_sort(arr) == sorted(arr)

def test_insertion_sort_shifts():
    arr = [2, 1, 3, 1, 2]
    assert 4 == insertion_sort_shifts(arr)