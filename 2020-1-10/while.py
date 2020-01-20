current_number = 1
while current_number <= 5:
    print(current_number)
    current_number+=1
prompt = "\n Tell me someting and I will repeat it back to you "
prompt +="\nEnter 'quit' to end this program "
message = ""
while message != 'quit':
    message = input(prompt)
    if message!='quit':
        print(message)
