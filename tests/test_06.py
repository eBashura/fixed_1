# Покрыть тестами функции в funcs_06

from funcs.funcs_06 import summ_and_max


def test_summ_args():
    result_1 = summ_and_max(2, 4, 6)
    assert result_1 == 12, 6
# не понимаю в чем тут ошибка