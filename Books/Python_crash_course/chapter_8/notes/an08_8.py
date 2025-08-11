unprinted_desingns = ['phone case', 'robot pendant', 'dodechaedron']
completed_models = [ ]
while unprinted_desingns:
    current_desing = unprinted_desingns.pop()
    print(f"printing model: {current_desing}")
    completed_models.append(current_desing)

print("\nThe following models have been printed:")
for completed_model in completed_models:
 print(completed_model)
