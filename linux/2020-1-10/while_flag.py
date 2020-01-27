prompt = "\n Tell me someting and I will repeat it back to you "
prompt +="\nEnter 'quit' to end this program "
active = True
#while active:
    #message = input(prompt)
    #if message == 'quit':
    #    active = False
    #else:
    #    print(message)
prompt = "\n please enter the name of city you have visited:"
prompt +="\nEnter 'quit' when you finished "
active = True
while True:
    city = input(prompt)
    if city == 'quit':
        break
    else:
        print("I don't love to go to"+city.title()+"!")

