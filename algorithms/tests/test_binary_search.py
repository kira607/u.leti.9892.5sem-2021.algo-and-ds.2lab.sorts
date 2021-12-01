from .. import binary_search

def test_binary_search():
    array = [i for i in range(0, 1000)]
    for i in range(0, 1000):
        assert binary_search(array, i) == i
    assert binary_search(array, -1) == -1
    assert binary_search(array, 1001) == -1
    
    array = [1,3,5,6,7,8]
    assert binary_search(array, 2) == -1
    assert binary_search(array, 8) == 5
    assert binary_search(array, 1) == 0