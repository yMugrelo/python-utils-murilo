place = []

print('please enter some places(not in alphabetic order): ')

for i in range(5):
    places = input(f'the place number {i + 1 }: ').title()
    place.append(places)


print(sorted(place))
print('\nstill the same result: ')
print(f"{place}\n")

print('reversing and showing how the list change\n ')
place.sort(reverse=True)
print(place)

print('turn back to the original\n')
place.sort(reverse=True)
print(place)