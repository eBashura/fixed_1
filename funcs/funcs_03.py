# Написать программу для нахождения факториала.
# Факториал натурального числа n определяется как произведение всех натуральных чисел от 1 до n включительно

def my_factorial(n):
    result = 1
    for number in range(1, n + 1):
        result *= number
    print(result)


my_factorial(5)
