# Покрыть тестами функции в funcs_05
import pytest

from funcs.funcs_05 import args_sum


def test_args_sum():
    result = args_sum(2, 3, 4)
    assert result == 11

