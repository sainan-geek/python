def get_formate_name(first_name,last_name):
    full_name=first_name+" "+last_name
    return full_name.title()
while True:
    print("\nPlease enter your name ")
    print("(enter 'q' at any time to quit)")
    f_name = input('First_name: ')
    if f_name =='q':
        break
    l_name = input('Last_name: ')
    if l_name =='q':
        break
    formate_name= get_formate_name(f_name,l_name)
    print("Hello "+formate_name+"!")
