# unprint_designs = ['iphone case','robot pendant','dodecahedron']
# completed_models = []

# while unprint_designs:
#     current_desigin = unprint_designs.pop()
#     print("printing model:"+current_desigin)
#     completed_models.append(current_desigin)
# print("\nThe following models have been printed:")
# for completed_model in completed_models:
#     print(completed_model)

def print_model (unprint_designs,completed_models):
    while unprint_designs:
        current_desigin = unprint_designs.pop()
        
        print("Printing model:"+current_desigin)
        completed_models.append(current_desigin)

def show_complete_modeles(completed_models):
    print("\nThe following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)
unprint_designs = ['iphone','robot pendant','dodecahedron']
completed_models= []
print_model(unprint_designs[:],completed_models)
for unprint_design in unprint_designs:
    print(unprint_design)

print("==========================================================================")

print_model(unprint_designs,completed_models)