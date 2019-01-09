cars =['audi','bmw','subaru','toyota']
for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())

requseted_topping = 'mushrooms'

if requseted_topping != 'anchovies':
    print("hold the anchovies")

age_0 = 22
age_1 = 18
if age_0>1 and age_1>3:
    print("it is true")

if age_0>1 or age_1<1:
    print("it is false")

if 'audi' in cars:
    print("Are you ok?")

car_nb = 'mw'
if car_nb not in cars:
    print(car_nb+" not in car")