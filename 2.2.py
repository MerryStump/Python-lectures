#абвгдеёжзиклмнопрстуфхцчшщъыьэюя
from itertools import count
glas = 0
alf = 'аеёиоуыэюя'
alf = tuple(alf)
stroka = str(input('Введите строку: '))
stroka.lower()
for i in range(len(stroka)):
    if stroka[i] in alf:
        glas += 1
print(f'Количество гласных в строке: {glas}')
