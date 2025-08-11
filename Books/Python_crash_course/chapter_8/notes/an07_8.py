def greet_user(names):
    for i in names:
        msg = f'Hello {i.title()}'
        print(msg)

names = ['margot', 'ty', 'hannah']
greet_user(names)
    