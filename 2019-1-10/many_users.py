users = {
    'aeinstein':{
        'first':'albert',
        'last':'einstein',
        'location':'princeton',
    },
    'mcurie':{
        'first':'marie',
        'last':'curie',
        'location':'paris',
    },
} 

for username,userinfo in users.items():
    print("username :"+username)
    full_name = userinfo['first'] +" "+ userinfo['last']
    location = userinfo['location']

    print("\tFullname: "+full_name.title())
    print("\tLocation  "+ location.title())
