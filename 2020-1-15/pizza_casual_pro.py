def make_pizza(size,*toppings):
    print("\nMaking a"+str(size)+"-inch pizza with the following toppings: ")
    for topping in toppings:
        print("-"+topping)

make_pizza(16,'a')
make_pizza(100,'x','y','z')
