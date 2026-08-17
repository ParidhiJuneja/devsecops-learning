from app.app import add, subtract, multiply, divide, square, is_even


def test_add():
    assert add(2, 3) == 5


def test_subtract():
    assert subtract(5, 2) == 3


def test_multiply():
    assert multiply(2, 3) == 6


def test_divide():
    assert divide(10, 2) == 5


def test_divide_by_zero():
    try:
        divide(10, 0)
        assert False
    except ValueError:
        assert True


def test_square():
    assert square(4) == 16


def test_is_even():
    assert is_even(4) is True