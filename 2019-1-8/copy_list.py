myfood = ['pizza','falafel','carrot cake']
friendfood=myfood[:]
print("\nfriendfood:")
for food in friendfood:
    print(food.title())
print("\nmyfood:")
for food in friendfood:
    print(food.title())
myfood.append('cannoli')
friendfood.append('ice cream')
print("\nfriendfood:")
for food in friendfood:
    print(food.title())
print("\nmyfood:")
for food in friendfood:
    print(food.title())