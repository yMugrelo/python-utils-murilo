def asking_sandwiches(sand):
    while True:
        sandwich = input("give the sanwich name:  ").lower()
        if sandwich == 'q':
            break
        sand.append(sandwich.title())
    
def printing_sand(sand):
    for i in sand:
        print(i)
sand = []

asking_sandwiches(sand)
printing_sand(sand)