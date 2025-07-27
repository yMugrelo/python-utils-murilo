prompt = 'please enter pizza flavors: '
pizzas = []
while True:
    pizza = input(prompt)
    if pizza == 'quit':
        break
    else:
        print(pizza)
        pizzas.append(pizza)

print("\n All the flavors: ")
for i in pizzas:
    print(f'\t{i}')