def print_models(unprinted_models, completed_models):
     while unprinted_models:
          current_models = unprinted_models.pop()
          print(f"printing models: {current_models}")
          completed_models.append(current_models)
def show_completed(completed_models):
     print("\n the following models have been printed: ")
     for i in completed_models:
          print(i.title())
unprinted_models = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []       
print_models(unprinted_models, completed_models)
show_completed(completed_models)