position = int(input("please enter your place in the race: "))
place = 0 
if position == 1:
    place+=1
    print(f"{place}st")
elif position == 2:
    place+=1
    print(f"{place}nd")
elif position == 3:
    place+=3
    print(f"{place}rd")

else:
    print(f"{position}th")

    