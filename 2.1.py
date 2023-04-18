sim = tuple(input('Введите по порядку, без пробелов, элементы кортежа: '))
print(sim)
for i in range(0, 9):
    if str(i) in sim:
         print(f'Количество {i} = ', sim.count(f'{i}'))