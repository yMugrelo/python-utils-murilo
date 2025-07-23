"""4-11. My Pizzas, Your Pizzas: Start with your program from Exercise 4-1
(page 56). Make a copy of the list of pizzas, and call it friend_pizzas.
Then, do the following:
•	 Add a new pizza to the original list.
•	 Add a different pizza to the list friend_pizzas.
•	 Prove that you have two separate lists. Print the message My favorite
pizzas are:, and then use a for loop to print the first list. Print the message
My friend’s favorite pizzas are:, and then use a for loop to print the second list. Make sure each new pizza is stored in the appropriate list."""

pizzas = ['frango', 'pepperoni', 'brocolis', 'mussarela']

friend_pizzas = pizzas[:]

print(f'my pizzas {pizzas}')
print(f'My friends pizzas {friend_pizzas}')
print("\n")
pizzas.append('picanha')
pizzas.append('da casa')

print(f"my pizzas changed {pizzas}")
print(f"my friend pizza changed {friend_pizzas}")