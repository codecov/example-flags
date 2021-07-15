from calculator import calculator


def test_add():
    assert calculator.add(1, 2) == 3


def test_subtract():
    assert calculator.subtract(1, 2) == -1
    

def test_div():
    assert calculator.divide(4, 2) == 2.0

    
def test_mult():
    assert calculator.multiply(4, 2) == 8
