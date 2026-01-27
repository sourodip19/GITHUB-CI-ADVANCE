from app import add
def test_add_positive():
    assert add(5,3) == 8

def test_add_negative():
    assert add(-5,-3) == -8