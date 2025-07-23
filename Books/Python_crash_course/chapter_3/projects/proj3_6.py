names = []
quant_table = int(input('\nHow many tables do you have at home? '))
quant_people = int(input('\nHow many people will come? '))
quant_space = quant_table * 4

if quant_space < quant_people:
    print('\nWe do not have space for all these people.')
else:
    for i in range(quant_people):
        name = input(f'\nInsert the name of person {i + 1}: ').title()
        names.append(name)

    print("\nGood news! We found a bigger dinner table! More space is available.")
    
    names.insert(0, "Gabriela")     
    names.insert(len(names)//2, "Sergio")  
    names.append("Vitoria")      

    print("\npdated Guest List & Invitations")
    for guest in names:
        print(f"\nDear {guest}, you are invited to dinner! Please join us.")