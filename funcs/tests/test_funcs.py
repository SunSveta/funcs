from funcs.get import get
from funcs.index_of import index_of
from funcs.slice import my_slice

def test_get():
    assert get([1, 2, 3], 1, "a") == 2
    assert get([4, 5, 6], 7, "val") == "val"
    assert get([4, 5, 6], 7) == None
    assert get([4, 5, 6], -7, 'negative') == 'negative'

def test_index_of():
    assert index_of([2, 7, 3, 2, 4], 2) == 0
    assert index_of([2, 7, 3, 2, 4], 9) == -1
    assert index_of([], 5) == -1
    assert index_of([2, 7, 3, 2, 4], 2, -7) == 0
    assert index_of([2, 7, 3, 2, 4], 4, -2) == 4

def test_slice():
    assert my_slice([1, 2, 3, 4, 5, 6], 1, 4) == [2, 3, 4]
    assert my_slice([1, 2, 3, 4, 5, 6], 2) == [3, 4, 5, 6]
    assert my_slice([], 2,4) == []
    assert my_slice([1, 2, 3, 4, 5, 6], -7, -2) == [1, 2, 3, 4]
    assert my_slice([1, 2, 3, 4, 5, 6], -3, -2) == [4]

