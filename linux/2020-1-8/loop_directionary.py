user_0 = {
    'username':'efermi',
    'first':'enrico',
    'last':'fermi',
}
for key,value in user_0.items():
    print('\nKey:'+ key)
    print('\nValue:'+value)

favorite_laguage={
    'jen':'python',
    'sarah':'c',
    'edward':'ruby',
    'phil':'python',
}
for name,language in favorite_laguage.items():
    print(name.title()+"'s favorite laguage is "+language.title()+".")

# .title()首字母大写标题化字符串
# .items()函数以列表返回可遍历的(键,值)元组数组
for name in favorite_laguage.keys():
    print(name.title())
print("**********************************************")
friends=['phil','sarah']
for name in favorite_laguage.keys():
    print(name.title())

    if name in friends:
        print("Hi "+name.title()+", I see you favorite language is "+ favorite_laguage[name].title()+"!")

if 'enric' not in favorite_laguage.keys():
    print("Erin, please take our poll!")