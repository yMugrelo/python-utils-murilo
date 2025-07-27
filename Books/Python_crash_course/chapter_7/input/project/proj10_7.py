prompt = "If you could visit one place in the world, where would you go?\n" 
prompt += " enter quit to stop the program: "
places = []
paz = True

while paz:
    
    place = input(prompt)
    if place == '':
        print("enter something ")
    if place.lower() == 'quit':
        paz = False
        break
    places.append(place)
    

if places:
    print("all the places: ")
    for i in places:
        print(f"\t - {i}")
else:
    print("no places were entered ")