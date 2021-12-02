from typing import List


def divide(array: List, left: int, right: int):
    pivot_value = array[right]
    middle_index = left - 1
    for i in range(left, right):
        if array[i] <= pivot_value:
            middle_index = middle_index + 1
            array[middle_index], array[i] = array[i], array[middle_index]
    array[middle_index + 1], array[right] = array[right], array[middle_index + 1]
    return middle_index + 1


def quick_sort(array: List, left: int = 0, right: int = None):
    right = len(array) - 1 if right is None else right
    if left < right:
        middle_index = divide(array, left, right)
        quick_sort(array, left, middle_index - 1)
        quick_sort(array, middle_index + 1, right)
    