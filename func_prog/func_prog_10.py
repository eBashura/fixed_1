# Создать lambda функцию, которая принимает на вход неопределенное количество именованных аргументов и выводит словарь
# с ключами удвоенной длины. {‘abc’: 5} -> {‘abcabc’: 5}


my_dict = (lambda **kwargs: {key * 2: value for key, value in kwargs.items()})(abc=3, bbb=5)
print(my_dict)
