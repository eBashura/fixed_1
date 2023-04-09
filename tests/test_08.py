# Покрыть тестами функции в funcs_08

from funcs.funcs_08 import arifmetik, geometrik, result_avg


def test_arifmet():
    result = arifmetik(3, 4, 5)
    assert result == 4


def test_geomet():
    result = geometrik(3, 4, 5)
    assert result == 3.9148676411688634


def res_average():
    result = result_avg(3, 4, 5, mean_type=0)
    assert result == 1

## не видит 3й тест