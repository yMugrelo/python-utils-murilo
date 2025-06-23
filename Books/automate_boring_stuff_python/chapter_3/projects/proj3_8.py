place = []

print('please enter some places(not in alphabetic order): ')

for i in range(5):
    places = input(f'the place number {i + 1 }: ').title()
    place.append(places)


print(sorted(place))
print('still the same result: ')
print(f"{place}\n")