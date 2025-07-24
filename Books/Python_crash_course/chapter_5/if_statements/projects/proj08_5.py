users = [
    'admin', 'Jorge',
    'Gabriel', 'Norman',
    'Maggie', 'Christian'
]

user_name = input("please enter you user name: ")

for i in users:
    if user_name.lower() == "admin":
        print(f"hello {user_name}")
        break
    elif user_name.title() == i:
        print(f"hello {user_name.title()}, thanks for logging again")
    else:
        print("we need to find some users ")
        