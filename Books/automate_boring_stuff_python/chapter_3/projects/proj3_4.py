# create a party list 
names = []


quantidade = int(input("how many people do you gonna invite "))


for i in range(quantidade):
    nome = input(f"put the name pearson {i+1}: ").title()
    names.append(nome)

cannot_come = names.pop(2)

print("\nthe party list is:")
for nome in names:
    print(f"- {nome}")

print(f'can not come to the party:\n {cannot_come}')


