def build_person(f_name, l_name, age= None):
    person = {
        'first' : f_name,
        'last': l_name
              }
    if age: 
        person['age'] = age
    return person
    
musician = build_person('jimi', 'handrix', 27 )
print(musician)