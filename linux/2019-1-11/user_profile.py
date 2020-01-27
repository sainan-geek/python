def bulid_profile(first,last,**user_info):
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key,value in user_info.items():
        profile[key] = value
    return profile

user_profile = bulid_profile('albert','eistenin',location='princeton',field='physics')
print(user_profile)
