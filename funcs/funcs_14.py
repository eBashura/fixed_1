# Описать функцию fact2( n ), вычисляющую двойной факториал :n!! = 1·3·5·...·n, если n — нечетное;
# n!! = 2·4·6·...·n, ё
# если n — четное. С помощью этой функции найти двойные факториалы пяти данных целых чисел

n = int(input("n = "))
start = 1 if n % 2 else 2
for i in range(start + 2, n + 1, 2):
    start *= i
print(start)
