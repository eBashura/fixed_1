# Покрыть тестами функции в funcs_06

from funcs.funcs_06 import summ_and_max


def test_summ_and_max():
    result = summ_and_max(1, 2, 3, 4)
    assert result == (10, 4)
