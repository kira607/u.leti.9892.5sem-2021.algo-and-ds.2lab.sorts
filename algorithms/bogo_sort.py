from random import randint


def is_sorted(array):
    n = len(array)
    for i in range(0, n-1):
        if array[i] > array[i + 1]:
            return False
    return True


def shuffle(array):
    n = len(array)
    for i in range(n):
        r = randint(0, n-1)
        array[i], array[r] = array[r], array[i]


def bogo_sort(array):
    while not is_sorted(array):
        shuffle(array)
