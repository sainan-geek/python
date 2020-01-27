def get_formatted_name(first_name,last_name,middle_name=""):#把middle_name变成可选的初始字符串设置为空并放到参数的最后面
    full_name = first_name+" "+middle_name+" "+last_name
    return full_name.title()
musician = get_formatted_name('davide','grate')
print(musician)
musician = get_formatted_name('davide','grate','lee')
print(musician)
