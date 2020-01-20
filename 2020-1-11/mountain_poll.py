responses={}
polling_active = True
while polling_active:
    name = input("\nWhat is your name? ")
    response = input("\nWhich mountain would you like to climb someday")
    responses[name]=response
    repet = input("Would you like let to another person response? (yes/no)")
    if repet == 'no':
        polling_active = False
    print("\n---Poll Results---")
    for name,response in responses.items():
        print(name+" Would you like to climb "+response+".")

