age = int(input("please enter your age: "))

if age <= 2:
    print("you are a baby ")

elif 2< age <=4 :
    print("you are a toodler ")

elif 4 < age <= 13:
    print("you are a kid")

elif 13 < age <= 20:
    print("teenager")
elif 20 < age <= 65:
    print("you are an adult")
else:
    print("you are an older")