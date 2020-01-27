def make_pizza(*toppings): #星号让python创建一个名为toppings的空元组并将收到的所有值都封装到这个元组中
    print("Making a pizza with following toppings: ")
    for topping in toppings:
        print("-"+topping)

make_pizza('a')
make_pizza('a','b','c','d')

