# задание макса 1

import datetime
from functools import wraps

limit = 10 ** 5


def my_decorator(func):
    @wraps(func)
    def inner(*args, **kwargs):
        start = datetime.datetime.utcnow()
        result = func(*args, **kwargs)
        finish = datetime.datetime.utcnow()
        print(finish - start)
        return result

    return inner


@my_decorator
def currentz(limit=10 ** 6):
    max_digit = 0
    max_steps = 0
    for digit in range(1, limit):
        current_steps = 0
        origin_digit = digit
        while digit != 1:
            if digit % 2:
                digit = (digit * 3 + 1) // 2
                current_steps += 2
            else:
                digit //= 2
                current_steps += 1
            # if not digit % 2:
            #     digit //= 2
            # else:
            #     digit = digit * 3 + 1
            # current_steps += 1
        if current_steps > max_steps:
            max_steps = current_steps
            max_digit = origin_digit
    print(max_digit, max_steps)
    return max_digit, max_steps


print(currentz())
