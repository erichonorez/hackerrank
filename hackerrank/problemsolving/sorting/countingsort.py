from typing import List

# https://www.hackerrank.com/challenges/countingsort1/problem

def countingsort_1(arr: List[int]) -> List[int]:
    """
    Returns an array of frequencies.
    """
    frequencies = [0 for i in range(0, 100)]

    for i in range(0, len(arr)):
        frequencies[arr[i]] += 1

    return frequencies


# https://www.hackerrank.com/challenges/countingsort2/problem

def countingsort(arr: List[int]) -> List[int]:
    """
    Returns an array of frequencies.
    """
    frequencies = [0 for i in range(0, 100)]

    for i in range(0, len(arr)):
        frequencies[arr[i]] += 1

    sorted = []
    for i in range(0, len(frequencies)):
        if frequencies[i] != 0:
            sorted[len(sorted):] = [i for j in range(0, frequencies[i])]

    return sorted

if __name__ == "__main__":
    print(countingsort_1([1, 2, 3, 3, 2, 0]))

