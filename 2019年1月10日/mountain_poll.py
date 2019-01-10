responses = {}

#Set a flag to indicate that polling is active
polling_active = True
while polling_active:
    name = input("\nWhat's your name ?")
    response = input("Which mountain would you like to climb someday?")
    responses[name] = response

    repeat = input("Would you like to let another person respond?(yes/no)")
    if repeat == 'no':
        polling_active = False
print("\n------Poll Result------")
for name,response in responses.items():
    print(name +" Would like to climb "+ response+".")
