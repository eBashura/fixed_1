import pytest

from funcs.funcs_03 import factorial

def test_factorial():
    result = factorial(3)
    assert result == 6

def test_type_error():
    with pytest.raises(TypeError):
        factorial("abc")


# def factorial(n: int) -> int:
#     result = 1
#     for i in range(1, n + 1):
#         result *= i
#     return result
#
# def test_factorial_5():
#     result = factorial(3)
#     assert result == 6
#
# def test_factorial_4():
#     result = factorial(4)
#     assert result == 24