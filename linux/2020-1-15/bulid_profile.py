def build_profile(first,last,**user_info):#一个星号元组两个星号字典
    profile={}
    profile['first_name'] = first
    profile['last_name'] = last
    for key,value in user_info.items():
        profile[key] = value
    return profile
 
user_profile=build_profile('albert','einstein',location = 'princeton',filed='physics')
print (user_profile)
