favorite_languages = {
    'jen' : 'python',
    'sarah' : 'c',
    'edward' : 'ruby',
    'phil' : 'python'
}

people_to_poll = ['jen', 'murilo', 'sarah', 'carlos', 'phil']

for person in people_to_poll:
    if person in favorite_languages:
        print(f"Thank you {person.title()}, for already taking the poll")
    else: 
        print(f"{person.title()}, please take our favorite language poll ")