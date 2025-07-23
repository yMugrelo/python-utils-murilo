quantify = int(input('How many pizzas do you want: '))

pizzas = []

for i in range(quantify):
    flavors = input(f"Enter the flavor number {i + 1}: ")
    pizzas.append(flavors)

print("My favorite flavors ")

for pizza in pizzas:
    print(f"I love {pizza.title()} pizza")

2
print('\n We all love pizza')

    


