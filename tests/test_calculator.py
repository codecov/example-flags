from calculator import calculator


def test_add():
    assert calculator.add(1, 2) == 3


def test_subtract():
    assert calculator.subtract(1, 2) == -1
