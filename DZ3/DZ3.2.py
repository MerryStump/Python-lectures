from random import randint

while True:
    p1k1 = randint(1, 6)
    p1k2 = randint(1, 6)
    if p1k1 == p1k2:
        print(F'{p1k1}, {p1k2}')
        break
    else:
        print('Lats try again')
while True:
    p2k1 = randint(1, 6)
    p2k2 = randint(1, 6)
    if p2k1 == p2k2:
        print(F'{p2k1}, {p2k2}')
        break
    else:
        print('Lats try again')
if (p1k1 + p1k2) > (p2k1 + p2k2):
    print('Player 1 wins')
elif (p1k1 + p1k2) < (p2k1 + p2k2):
    print('Player 2 wins')
else:
    print('Ничья')
