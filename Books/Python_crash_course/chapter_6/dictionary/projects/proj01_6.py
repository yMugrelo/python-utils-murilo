person = {
    'name' : ' Carlos ',
    'last name': ' ',
    'age' :'24',
    'city' : 'manaus',

}

person['last name'] = input(f"please enter the {person['name']} last name: ").title()

print(f"the person name is {person['name']}")
print(f"the person's last name is {person['last name']}")
print(f"the person's age is {person['age']}")
print(f"the person city is {person['city'].title()}")



