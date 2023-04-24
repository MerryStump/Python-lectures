from random import choice
list4 = ['Чтение', 'Пение', 'Рисование', 'Математика']
list8 = ['Литература', 'Математика', 'Русский язык', 'Окружающий мир', 'Музыка', 'Труд', 'Химия', 'Физика']
list12 = ['Химия', 'Физика', 'Алгебра', 'Геометрия', 'Биология', 'Физ-ра', 'Литература', 'Русский язык', 'Информатика', 'ОБЖ', 'География', 'Английский язык']
week = ['Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница']
n = []
klass=int(input('Введите номер класса\t'))
for i in range (5):
    if 1<=klass<=4:
        for j in range(4):
            a = choice(list4)
            n.append(a)
        print(f'{week[i]}: {n}')
        n = []
    elif 5<=klass<=8:
        for j in range(8):
            a = choice(list8)
            n.append(a)
        print(f'{week[i]}: {n}')
        n = []
    elif 9<=klass<=11:
        for j in range(12):
            a = choice(list12)
            n.append(a)
        print(f'{week[i]}: {n}')
        n = []
    else:
        print('Такого класса не существует, попробуйте снова')