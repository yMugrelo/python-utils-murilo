pizza = {
 'crust': 'thick',
 'toppings': ['mushrooms', 'extra cheese'],
 }


print(f"You ordered a {pizza['crust']}")
for topping in pizza['toppings']:
    print("\t" + topping)