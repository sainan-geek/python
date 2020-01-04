filename = 'E:\\make the change\\python\\2019年1月13日\\programming.txt'

# with open(filename,'w')as file_object:
#     file_object.write("I love programming\n")
with open(filename,'a')as file_object:             #实参a
    file_object.write("I love programming\n")
n=5
number = list(range(1,1000))                                #python生成一个1到n的队列
with open(filename,'a')as file_object:             #实参a
    file_object.write(str(number))