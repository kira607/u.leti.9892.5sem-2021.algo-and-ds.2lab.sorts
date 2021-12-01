from algorithms import binary_search


def main():
    array = [i for i in range(0, 1000)]
    for i in range(0, 1000):
        print(i)
        assert binary_search(array, i) == i
    assert binary_search(array, -1) == -1
    assert binary_search(array, 1001) == -1
    
    array = [1,3,5,6,7,8,9,10,11,12,13]
    assert binary_search(array, 2) == -1
    assert binary_search(array, 3) == 1


if __name__ == '__main__':
    main()