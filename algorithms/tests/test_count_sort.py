from random import randint

import pytest

from algorithms import count_sort


def test_count_sort_random():
    array = [randint(-100, 100) for _ in range(100_000)]
    copy = count_sort(array, -100, 100)
    array.sort()
    assert copy == array


def test_count_sort_static():
    array = [2, 7, 2, 1, 5, 5, 4, 12, 0, 9, -4]
    array = count_sort(array)
    assert array == [-4, 0, 1, 2, 2, 4, 5, 5, 7, 9, 12]


def test_count_sort_static_with_exception():
    array = [2, 7, 2, 1, 5, 5, 4, 12, 0, 9, -4]
    with pytest.raises(ValueError):
        count_sort(array, 0, 100)
