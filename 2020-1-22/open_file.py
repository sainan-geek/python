file_path='/home/sainan/PycharmProjects/python/2020-1-21/pi_digitals.txt'
#with open(file_path) as file_object:
#    contents = file_object.read()
#    print(contents.rstrip())
#    for line in file_object:
#        print(line.rstrip())
print("===================================")
with open(file_path) as file_object_two:
    lines = file_object_two.readlines()

for line in lines:
    print(line.rstrip())
