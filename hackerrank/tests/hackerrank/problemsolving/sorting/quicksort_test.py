from hypothesis import given, strategies as st
from hackerrank.problemsolving.sorting.quicksort import quicksort


@given(arr=st.lists(st.integers(), max_size=100))
def test_insertion_sort(arr):
    assert quicksort(arr) == sorted(arr)