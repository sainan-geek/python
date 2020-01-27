def build_person(first_name,last_name,age=''):
    person={'first':first_name,'last':last_name}
    if age:
        person['age'] = age
    return person
while True:
    print("Please tell me your name:")
    f_name = input("\nFirst_name: ")
    l_name = input("\nLast_name: ")
    musician=build_person(f_name,l_name)
#musician = build_person('jimi','hendrix',age=13)
    print(musician)
