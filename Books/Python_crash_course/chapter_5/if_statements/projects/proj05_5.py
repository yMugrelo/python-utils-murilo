alien_color = input("please enter the alien color: ")
points = 0
if alien_color.lower() == "green":
    points += 5
    print(f"the player earned {points} points") 

elif alien_color.lower() == "yellow":
    points+= 10
    print(f"the player earned {points} points") 

elif alien_color.lower() == "red":
     points+= 15
     print(f"the player earned {points} points") 

else:
    print(f"put one of the three colors: {alien_color}")