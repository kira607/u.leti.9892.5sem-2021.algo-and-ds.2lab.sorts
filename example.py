from algorithms import (
    count_sort,
    quick_sort,
    insertion_sort,
    bogo_sort,
    binary_search,
)


def main():
    print(count_sort([9, 9, 8, 4, 3, 2, 0, 10]))
    a = [-1, 6, 3, 1, 7, 5, 2, 6]
    quick_sort(a)
    print(a)
    a = [-1, 6, 3, 1, 7, 5, 2, 6]
    insertion_sort(a)
    print(a)
    a = [-1, 6, 3, 1, 7, 5, 2, 6]
    bogo_sort(a)
    print(a)
    print(binary_search(a, 1))
    print(binary_search(a, 3))
    print(binary_search(a, 7))
    print(binary_search(a, -1))
    print(binary_search(a, 100))
    print(binary_search(a, 0))


if __name__ == '__main__':
    main()
