def fun(a):  # ну тут идентично, лишь + строчка
    sum = 0
    l = len(list)
    for i in range(l):
        sum += list[i]
        list[i] = sum
    return sum


list = []
while True:
    vvod = input('Введите число. Для остановки введите "Стоп":\t')
    if vvod == 'Стоп':
        break
    else:
        vvod = int(vvod)
        list.append(vvod)
print(f'Результат произведения: {fun(list)}')
print(list)
