def describ_pets(animal_type,pet_name='tom'): #调用时一定要有实参
    print("\nI hava a "+animal_type.title()+".")
    print("My "+animal_type.title()+" name is "+pet_name.title()+".")
describ_pets('hamster','harry')
describ_pets('dog','willie')
describ_pets(animal_type='cat',pet_name='amy')
describ_pets(animal_type='pig')
describ_pets('penguin')
