cs=[]
for i in range(10):
    n=str(input('Введите название города\t'))
    if n=='стоп' or n=='Стоп':
        break
    elif n in cs:
        print('Такой город уже есть в списке')
    else:
        cs.append(n)
print(cs)