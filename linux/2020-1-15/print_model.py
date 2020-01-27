def print_models(unprint_designs,complete_models):
    while unprint_designs: 
          current_print=unprint_designs.pop()
          print("Printing models "+current_print)
         
         complete_models.append(current_print)

unprint_designs=['a','b','c','d']
complete_models=[]
print_models(unprint_designs[:],complete_models)

for complete_model in complete_models:
    print("There are complete models "+complete_model)

