from typing import List

# https://www.hackerrank.com/challenges/closest-numbers/problem

def closest_numbers(arr: List[int]) -> List[int]:
    sorted_arr = sorted(arr)
    
    smallest_abs_diff_so_far = None
    for i in range(0, len(sorted_arr) - 1):
        diff = abs(sorted_arr[i + 1] - sorted_arr[i])
        if smallest_abs_diff_so_far == None \
            or smallest_abs_diff_so_far > diff:
            smallest_abs_diff_so_far = diff

    result = []
    for i in range(0, len(sorted_arr) - 1):
        if (abs(sorted_arr[i + 1] - sorted_arr[i])) == smallest_abs_diff_so_far:
            result.append(sorted_arr[i])
            result.append(sorted_arr[i + 1])
    
    return result

if __name__ == "__main__":
    print(closest_numbers([-20, -3916237, -357920, -3620601, 7374819, -7330761, 30, 6246457, -6461594, 266854, -520 ,-470]))
