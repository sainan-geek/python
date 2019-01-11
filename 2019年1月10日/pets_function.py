def describe_pet(animal_type,pet_name):
    print("\nI have a "+animal_type+".")
    print("My " +animal_type+ "'s name is " + pet_name.title()+".")

describe_pet('hamster','harry')
describe_pet('dog','willie')

describe_pet(pet_name='harry',animal_type='hamster')
print("==========================================")

def describe_pet1(pet1_name,animal1_type='dog'):
    print("\nI have a "+animal1_type+".")
    print("My " +animal1_type+ "'s name is " + pet1_name.title()+".")

describe_pet1(pet1_name='willie')