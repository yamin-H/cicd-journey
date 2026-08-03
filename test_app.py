from app import add, subtract, multiply

def test_add_positive_numbers():
    assert add(2, 3) == 5

def test_add_negative_numbers():
    assert add(-1, -1) == -2

def test_add_zero():
    assert add(0, 5) == 5

def test_subtract_basic():
    assert subtract(10, 4) == 6

def test_subtract_gives_negative():
    assert subtract(3, 10) == -7

def test_multiply_basic():
    assert multiply(3, 4) == 12

def test_multiply_by_zero():
    assert multiply(5, 0) == 0