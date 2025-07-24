answer = 17

c_n = int(input("try to enter the right number"))

while c_n != answer:
    if answer == c_n:
       print("WIN")

    elif answer > c_n:
        print("the number is higher")
    elif answer < c_n:
        print("the number is lower")
    c_n = int(input("try to enter the right number"))


print("WIN")
