# Покрыть тестами функции в funcs_07

from funcs.funcs_07 import chetnie


def test_chetnie_li():
    result = chetnie(abcfd=2, bbbb=5, cdfagadg=6, ababab=10)
    assert result == {'bbbb': 5, 'cdfagadg': 6, 'ababab': 10}


def test_net_chetnix():
    result = chetnie(abd=2, bbb=5, cdfgadg=6, babab=10)
    assert result == {}
