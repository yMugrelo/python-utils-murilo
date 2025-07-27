prompt = 'please enter your age: '
print("the number 1000 stops the program")
total_price = 0
while True:
    age = int(input(prompt))
    age = int(age)

    if age == 1000:
        break
    if age <= 3:
        print("the ticket is free")
        total_price+=0
    elif 3 < age < 12:
        print("the ticket cost 10 dollars ")
        total_price+=10
    elif age > 12:
        print('the ticket cost 15 dollars')
        total_price += 15
print(f"The cost of your ticket is {total_price}")
