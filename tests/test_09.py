# Покрыть тестами функции в funcs_09

from funcs.funcs_09 import equal_number


def test_quantity_of_equal_numbers(arr):
    result = test_quantity_of_equal_numbers(1, 2, 1, 4, 5, 6, 7)
    assert result == 2
