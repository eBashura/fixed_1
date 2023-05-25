# Покрыть тестами функции в funcs_11


from funcs.funcs_11 import *


def test_is_power_n_true():
    result = is_power_n(9, 3)
    assert result == True


def test_is_power_n_false():
    result = is_power_n(11, 3)
    assert result == False
