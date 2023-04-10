# Покрыть тестами функции в funcs_05
import pytest

from funcs.funcs_05 import args_sum


def test_args_sum():
    result = args_sum(2, 3, 4)
    assert result == 11


def test_type_error():  ## проверка на ввод некорректных данных, правильно ли? т.к. в тесте самом пишет, что был только 1 тест выполнен
    with pytest.raises(TypeError):
        args_sum(2, 3, 'abc')