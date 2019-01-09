#使用for循环遍历字典
user_0 = {
    'username':'efermi',
    'first':'enrico',
    'last':'fermi',
}
for key,value in user_0.items():
    print("\nKey " + key)
    print("Value " + value)
print("====================================================")
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

for name,language in favorite_languages.items():
     print(name.title()+"'s favorite language is "+ language.title()+".")
print("====================================================")
for name in favorite_languages.keys():
    print(name.title())


for name in favorite_languages:
    print(name.title())
print("====================================================")
friends = ['phil','sarah']
for name in favorite_languages.keys():
    print(name.title())

    if name in friends:
        print(" Hi "+ name.title()+", I see your favorite language is "+ favorite_languages[name].title()+"!")

if 'erin' not in favorite_languages.keys():
    print("Erin please take out poll")

for name in sorted(favorite_languages.keys()):
    print(name.title()+" , thank you for taking the roll")

print("====================================================")
print("The following languages have been mentioned:")
for language in favorite_languages.values():
    print(language.title())

print("====================================================")
for language in set(favorite_languages.values()):
    print(language.title())