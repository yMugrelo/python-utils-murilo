users = {
    'aeinstein' :{
        'name' : 'albert',
        'last name' : 'einstein',
        'location' : 'princeton '
    },
    'mcurie' : {
        'name' : 'marie',
        'last name' : 'curie',
        'location' : 'paris',
    },
}

for user, info in users.items():
    print(f"\n username: {user}")
    full_name = f"{info['name']} {info['last name']}"
    location = info['location']
    print(f"\t fullname = {full_name}")
    print(f"\t location: {location}")
