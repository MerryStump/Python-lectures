from itertools import zip_longest
name=['Ricky', 'Kek']
age=[12, 6]
animal=['Dog', 'Cat']
while True:
    print('\n\t{:^20}\t{:^4}\t{:^16}\n'.format('Name', 'Age', 'Animal'))
    for i, j, k in zip_longest(name, age, animal):
        print('\t{:^20}\t{:^4}\t{:^16}'.format(i,j,k))
    n=str(input('\nDo you want to add or delete a pet? (Enter "Break" for exit):\t'))
    n.lower()
    if n=='add':
        name.append(str(input('\nEnter the pets name (For example: Barsik):\t')))
        age.append(int(input('\nEnter the pats age:\t')))
        animal.append(str(input('\nEnter the type of pet (For example: Cat)\t')))
    elif n=='exit':
        break
    elif n=='delete':
        a=input('\nEnter the name of the pet you want to delete:\t')
        a.lower()
        l=len(name)
        for i in range(l):
            if a==name[i]:
                del name[i]
                del age[i]
                del animal[i]
                break
    else:
        print('Sorry, the word is not recognized, please try again')
