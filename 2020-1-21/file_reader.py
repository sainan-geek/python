with open('pi_digitals.txt') as file_object:
    contents = file_object.read()
    print(contents) #read 到达文件末尾时会返回一个空字符串　空字符串显示出来就是一个空行
    print(contents.rstrip())#.rstrip删除空行
