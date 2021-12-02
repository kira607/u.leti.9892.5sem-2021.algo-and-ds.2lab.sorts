from random import randint

from algorithms import insertion_sort


def test_insertion_sort_random():
    array = [randint(-100, 100) for _ in range(100)]
    copy = array[:]
    insertion_sort(copy)
    array.sort()
    assert copy == array


def test_insertion_sort_static():
    array = [2, 7, 2, 1, 5, 5, 4, 12, 0, 9, -4]
    insertion_sort(array)
    assert array == [-4, 0, 1, 2, 2, 4, 5, 5, 7, 9, 12]