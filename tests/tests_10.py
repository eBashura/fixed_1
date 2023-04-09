# Покрыть тестами функции в funcs_10

from funcs.funcs_10 import kvadrat_uravnenie


def test_kvadrat_urav():
    result = kvadrat_uravnenie(2, 3, 4)
    assert result == -0.25, -1.25
# не понимаю что не так