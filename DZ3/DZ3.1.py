print('\t\t\tТаблица умножения\n\t\t1\t\t2\t\t3\t\t4\t\t5\t\t6\t\t7\t\t8\t\t9\t\t10')
for i in range(1, 11):
    print(F'\n{i}\t', end='')
    for j in range(1, 11):
        n = i * j
        print(F'{i}*{j}={n}\t', end='')
