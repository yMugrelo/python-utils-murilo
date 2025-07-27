cars = ['subaru', 'mercedez','ferrari', 'porsche']
m_car = input("please enter a car: ")

print(f"let me see if i can find a {m_car}")
found = False
for i in cars:
    if i == m_car.lower():
        print(f"we have your car: {m_car.title()} ")
        found = True
        break

if not found:
    print("We do not have your car")


