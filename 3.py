def fun(a):  # создание функции
    pr = 1
    l = len(list)
    for i in range(l):
        pr *= list[i]
    return pr


list = []
while True:
    vvod = input('Введите число. Для остановки введите "Стоп":\t')
    if vvod == 'Стоп':
        break
    else:
        vvod = int(vvod)
        list.append(vvod)
print(f'Результат произведения: {fun(list)}')  # в конце скармливаем созданный список функции
