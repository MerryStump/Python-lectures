import random as r
import math as m
a=0
b=0
x=int(input('Введите X\t'))
for i in range(x):
    n=r.randint(1, 100)
    print(n)
    t=m.fmod(n,2)
    if t==0:
        a+=n
    else:
        b+=n
print(F'Сумма четных чисел: {a}', F'Сумма нечетных чисел: {b}')