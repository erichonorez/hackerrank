from hypothesis import given, strategies as st
from problemsolving.sorting.countingsort import countingsort
from itertools import groupby

@given(arr=st.lists(st.integers(min_value=0, max_value=99), max_size=100))
def test(arr):
    assert countingsort(arr) == sorted(arr)
