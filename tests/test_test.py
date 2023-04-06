def summ(a, b):
    if a > b:
        return a + b + 1
    elif a < b:
        return a + b - 1
    else:
        return a + b


def test_sum_a_is_bigger_b():
    result = summ(3, 2)
    assert result == 6


def test_sum_a_less_b():
    result = summ(1, 2)
    assert result == 2


def test_sum_a_equal_b():
    result = summ(2, 2)
    assert result == 4
