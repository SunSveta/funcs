from stars.get_value import get_val

def test_get_val():
    assert get_val({1:'Show', 2:'must', 3:'go on'}, 3, 'Queen') == 'go on'

def test_get_val():
    assert get_val({1:'Show', 2:'must', 3:'go on'}, 5, 'Queen') == 'Queen'


def test_ampty_coll():
    assert get_val({}, 2, 'Wtf') == 'Wtf'

def test_ampty_default():    
    assert get_val({1:'Show', 2:'must', 3:'go on'}, 5) == None


