age = int(input("Please enter your age: "))

if age < 18:
    print("You cannot vote.\n")

elif age >= 18:
    print("You are old enough to vote.\n")
    
    r = input("Have you registered to vote yet? (Yes or No): ")
    
    if r.lower() == 'yes':
        print("OK")
    elif r.lower() == 'no':
        print("Please go to our website to register.")
    else:
        print("Please enter a valid response (Yes or No).")
else:
    print("i`m sorry you`re too young to vote ")
    print("please register to vote as soon as you turn 18")
