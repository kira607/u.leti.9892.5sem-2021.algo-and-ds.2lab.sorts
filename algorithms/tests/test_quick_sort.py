from random import randint

from algorithms import quick_sort


def test_quick_sort_random():
    array = [randint(-100, 100) for _ in range(100)]
    copy = array[:]
    quick_sort(copy)
    array.sort()
    assert copy == array


def test_quick_sort_static():
    array = [2, 7, 2, 1, 5, 5, 4, 12, 0, 9, -4]
    quick_sort(array)
    assert array == [-4, 0, 1, 2, 2, 4, 5, 5, 7, 9, 12]
