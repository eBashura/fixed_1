# Покрыть тестами функции в funcs_07

from funcs.funcs_07 import chetnie


def test_chetnie_li():
    result = chetnie(abcfd=2, bbbb=5, cdfagadg=6, ababab=10)
    assert result == 'bbbb=5' and 'cdfagadg=6' and 'ababab=10'
# не понимаю что не так