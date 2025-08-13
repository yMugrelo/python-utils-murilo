def make_pizza(*toppings):
    print("making a pizza with the following requests: ")
    for i in toppings:
        print(i)
    
make_pizza('peperonni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')
