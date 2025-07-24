alien_color = [
    'yellow','green',
    'red'
    ]

points = 0 
alien = input("enter the alien color: ")
for i in alien_color:
    if alien.lower() == i:
        points+=5
    else:
        points+=10 

print(f"you earned {points} points")