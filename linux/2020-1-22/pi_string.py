file_name = 'pi_million_digits.txt'
with open(file_name) as file_object:
    lines = file_object.readlines()

pi_string = ''
for line in lines:
    pi_string += line.strip()
print(pi_string[:52] + '.......')
print(len(pi_string)) 
birthday = input("Please input your birthday,in the form mmyydd: ")
if birthday in pi_string:
    print("Your birthday appears in the first million digitals of pi!")
else:
    print("Your birthday dose not appear in the first million digits of pi.")
