def make_album():
    albuns = {}
    for i in range(3):
        al_name = input("Please enter the album name: ")
        ar_name = input("Enter the artist name: ")
        description = input("Please enter a description about this album: ")

        albuns[al_name] = {
            "artist": ar_name,
            "description": description
        }

    for index, (al_name, info) in enumerate(albuns.items(), start=1):
        print(f"{index}. The album '{al_name.title()}' from artist '{info['artist'].title()}'")
        print(f"   Has this description: {info['description']}\n")

make_album()
