file_path='/home/sainan/PycharmProjects/python/2020-1-21/pi_digitals.txt'
with open(file_path) as file_object:
    lines = file_object.readlines()

pi_string = ''
for line in lines:
    pi_string += line.rstrip()
print(pi_string)
print(len(pi_string))
