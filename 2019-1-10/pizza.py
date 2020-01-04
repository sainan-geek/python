#字典中元素遍历 

pizza = {
    'crust':'trick',
    'toppings':['mushrooms','extra cheese'],
}
print("You order a " +pizza['crust']+"-crust pizza "+"with the following toppings:")

for topping in pizza['toppings']:
    print("\t"+topping)

print("=============================================================================")
favorite_langugaes = {
    'jen':['python','ruby'],
    'sarah':['c'],
    'edward':['ruby','go'],
    'phil':['python','haskell'],
}
for name,languages in favorite_langugaes.items():
    print("\n"+name.title()+"'s favorite language are:")
    for language in languages:
        print("\t"+ language.title())