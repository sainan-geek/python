filename = 'programming.txt'

with open(filename,'w') as file_object: #w是写入模式
    file_object.write("hello world.\n")
    file_object.write("hello China.\n")
with open(filename,'a') as file_object1:
    file_object1.write("sa")
