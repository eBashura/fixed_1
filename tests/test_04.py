# Покрыть тестами функции в funcs_04

from funcs.funcs_04 import create_matrix, create_matrix2


def test_create_matrx():
    result = create_matrix(3, random_from=1, random_to=9)
    assert result

# def test_create_matrix_2():
#     result = create_matrix2(3, random_from=1, random_to=9)
#     assert result