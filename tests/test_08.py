# Покрыть тестами функции в funcs_08

from funcs.funcs_08 import *


def test_avg_arifm():
    result = arifmetik(3, 4, 5)
    assert result == 4


def test_avg_geom():
    result = geometrik(3, 4, 5)
    assert result == 3.9148676411688634


def test_result_avg_arifm():
    result = result_avg(3, 4, 5, mean_type=0)
    assert result == 4


def test_result_avg_geom():
    result = result_avg(3, 4, 5, mean_type=1)
    assert result == 3.9148676411688634
