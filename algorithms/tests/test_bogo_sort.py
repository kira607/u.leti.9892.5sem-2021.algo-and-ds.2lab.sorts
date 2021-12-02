from random import randint

from algorithms import bogo_sort


def test_bogo_sort_random():
    array = [randint(-100, 100) for _ in range(5)]
    copy = array[:]
    bogo_sort(copy)
    array.sort()
    assert copy == array


def test_bogo_sort_static():
    array = [2, 7, 2, 1, 5, -4]
    bogo_sort(array)
    assert array == [-4, 1, 2, 2, 5, 7]
