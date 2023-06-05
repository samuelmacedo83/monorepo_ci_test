from project2.multiply_numbers import multiply_numbers

def test_multiply_numbers():
    result = multiply_numbers(2, 3)
    assert result == 6

def test_multiply_numbers():
    result = multiply_numbers(3, 3)
    assert result == 9

def test_multiply_numbers():
    result = multiply_numbers(4, 3)
    assert result == 12
