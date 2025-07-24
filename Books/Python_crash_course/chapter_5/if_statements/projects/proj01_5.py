cars = [
    'subaru', 'ferrari'
    'nissan', 'peugeot',
    'renault', 'fiat'
        
        ]

user_car = input("please enter your car ").lower()

for car in cars:
    if car == user_car:
        print(f"you have one of the car list: {cars}\nyour car is a {user_car}")


    