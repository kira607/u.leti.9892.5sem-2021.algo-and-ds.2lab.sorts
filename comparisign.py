import time

import matplotlib.pyplot as plt
from tqdm import tqdm

from algorithms import quick_sort, insertion_sort


def random_array(size, left=-100, right=100):
    from random import randint
    array = [randint(left, right) for _ in range(size)]
    return array


def main():
    original_ranges = [i for i in range(0, 3000)]
    original_ranges.extend([i for i in range(5000, 6000, 10)])
    original_ranges.extend([i for i in range(10000, 50000, 1000)])
    # original_ranges.extend([i for i in range(50000, 100000, 1000)])
    # original_ranges = (1, 10, 100, 1000)
    repeat = 2
    iters = []
    for value in original_ranges:
        for _ in range(repeat):
            iters.append(value)

    fig, ax = plt.subplots()
    ax.grid(True)

    x = []
    y = []
    for i in tqdm(iters):
        x.append(i)
        array = random_array(i)
        t = time.time()
        quick_sort(array)
        t = time.time() - t
        y.append(t)

    ax.scatter(x, y, color='red', alpha=0.5, label='quick_sort', edgecolors='none')

    x = []
    y = []
    for i in tqdm(iters):
        x.append(i)
        array = random_array(i)
        t = time.time()
        insertion_sort(array)
        t = time.time() - t
        y.append(t)

    ax.scatter(x, y, color='blue', alpha=0.5, label='insertion_sort', edgecolors='none')

    ax.legend()

    plt.show()


if __name__ == '__main__':
    main()
