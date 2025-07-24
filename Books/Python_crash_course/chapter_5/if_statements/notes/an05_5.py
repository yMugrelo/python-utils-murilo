banned_users = [
    'andrew', 'carolina',
    'david'
]

user = 'maria'

for i in banned_users:
    if user != i:
        print(f"{user.title()}, you can post a response if you wish \n")