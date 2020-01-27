from collections import OrderedDict

favorite_language = OrderedDict()

favorite_language['jen']='python'
favorite_language['srarh'] ='c'
favorite_language['edward'] ='ruby'
favorite_language['phil'] = 'python'

for name,language in favorite_language.items():
    print(name.title()+" 's favorite language is "+language.title()+".")

