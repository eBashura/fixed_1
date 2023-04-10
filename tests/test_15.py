# Покрыть тестами функции в funcs_15

from funcs.funcs_15 import polindrom_2


def test_polindrom():
    result = polindrom_2('assa')
    assert result == True


def test_polindrom_false():
    result = polindrom_2('ass')
    assert result == False
