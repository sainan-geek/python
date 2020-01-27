favorite_laguage={
    'jen':['python','ruby'],
    'sarah':['c'],
    'edward':['ruby','go'],
    'phil':['python','haskell'],
}
for name,languages in favorite_laguage.items():
    print("\n"+name.title()+"'s favorite language are:")
    for language in languages:
        print("\t"+language.title())
print("*********************************")
users = {                #字典{}列表[]
    'asinstein':{
        'first':'albert',
        'last':'einstein',
        'location':'paries',
    },
    'mcurie':{
        'first':'marial',
        'last':'curie',
        'location':'paries',
    },
}
for username,user_info in users.items():
    print("\nUnsername: "+username)
    fullname = user_info['first']+" "+user_info['last']
    location = user_info['location']
    print('\tFull name: '+fullname.title())
    print('\tLocation: '+location.title())
