from random import randint
orel = 0
reshka = 0
for i in range(1000):
    n = randint(0, 1)
    if n == 0:
        orel += 1
    else:
        reshka += 1
print('В итоге выпало: орлов {:.2%}, решек {:.2%}'.format(orel/1000, reshka/1000))