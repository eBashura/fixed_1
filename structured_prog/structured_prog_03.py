# Получить на ввод количество рублей и копеек и вывести в правильной форме, например, 3 рубля, 1 рубль 25 копеек, 3 копейки

quant_rub = int(input('введите рубли '))
quant_cop = int(input('введите копейки '))
if quant_rub != 0 and quant_cop != 0:
    print(f'{quant_rub} руб {quant_cop} коп')
elif quant_rub != 0 and quant_cop == 0:
    print(f'{quant_rub} руб')
else:
    print(f'{quant_cop} коп')
