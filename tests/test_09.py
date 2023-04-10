# Покрыть тестами функции в funcs_09

from funcs.funcs_09 import *


def test_counter_numbers_in_list():
    result = equal_number(1, 3, 1, 2, 3)
    assert result == {'1': 2, '2': 1, '3': 2}
