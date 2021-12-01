from typing import Any, Iterable

def binary_search(iterable: Iterable, value: Any, left=0, right=None):
    try:
        right = len(iterable) if right is None else right
        while left <= right:
            middle = left + ((right - left) // 2)
            if iterable[middle] == value:
                return middle
            elif iterable[middle] < value:
                left = middle + 1
            else:
                right = middle - 1
        return -1
    except IndexError:
        return -1
