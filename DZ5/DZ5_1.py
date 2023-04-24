from itertools import zip_longest
name = ['Vitaly', 'Dima', 'Rick', 'Morty', 'Luke', 'Darth', 'Tomas', 'Cheburator', 'Gena', 'Ded']
fam = ['Semushkin', 'Kozhevnikov', 'Sanches', 'StupidPoS', 'Skywalker', 'Vader', 'Shelby', 'Ushastiy', 'Buckin', 'Bom-Bom']
for i, j in zip_longest(name, fam):
    print(i, j)
