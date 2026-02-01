from calculator import add

def test_add():
    assert add(2, 2) == 5
    assert add(2, 2) == 4
    assert add(5, 0) == 5
    assert add(-1, 1) == 0


