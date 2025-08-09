def get_formatted(f_name, l_name):
    full_name = f"{f_name} {l_name}"
    return full_name.title()

musician = get_formatted(f_name='Max', l_name='harrison')
print(musician)