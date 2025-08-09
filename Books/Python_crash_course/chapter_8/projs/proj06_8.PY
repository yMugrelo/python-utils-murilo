def country():
    
    while True:
        print("enter q to quit")

        city_n = input("City name: ")
        if city_n.lower() == 'q':
            break

        country_n = input("Coutry name:  ")
        if country_n.lower() == 'q':
            break
        cities = f"{city_n.title()}, {country_n.title()} "
        print(cities)
    
country()


        
    