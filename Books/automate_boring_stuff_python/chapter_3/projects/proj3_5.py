names = []

quant = int(input('how many people will be with us:  '))


for i in range(quant):
    nome = input(f'\ninsert the person {i + 1}: ')
    names.append(nome)

print("\nCurrent list of people:", names)
    
non_called = int(input('insert how many people cannot come: '))


for i in range(non_called):
    if names:
        name = input(f'enter the name who cannot come: ')
        if name in names:
            names.remove(name)

        else:
            print(f'{name} not found in the list')

print('\n end of the list')

print(names)



print(names)