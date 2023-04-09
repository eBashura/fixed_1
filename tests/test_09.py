# Покрыть тестами функции в funcs_09
from random import randint

from funcs.funcs_09 import equal_number


def test_quantity_of_equal_numbers():
    result = test_quantity_of_equal_numbers([randint(1, 10) for _ in range(6)])
    assert result == 2
# не понимаю как делать