def cities():
    cities = {}
    for i in range(3):
        city_name = input("Please enter your city name: ")
        country = input("please enter your country name: ")
        cities[city_name] = country

    
    for index, (city, countrie) in enumerate(cities.items(), start = 1):
        print(f"{index}. {city.title()} is in {countrie.title()}")

cities()

