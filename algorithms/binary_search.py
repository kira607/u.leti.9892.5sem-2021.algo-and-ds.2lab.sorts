from typing import Any


def binary_search(array, value: Any, left=0, right=None):
    try:
        right = len(array) if right is None else right
        while left <= right:
            middle = left + ((right - left) // 2)
            if array[middle] == value:
                return middle
            elif array[middle] < value:
                left = middle + 1
            else:
                right = middle - 1
        return -1
    except IndexError:
        return -1
