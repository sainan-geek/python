favorite_laguage={
    'jen':'python',
    'sarah':'c',
    'edward':'ruby',
    'phil':'python',
}
for name in favorite_laguage.keys():
    print(name.title()+", thank you for taking the poll.")
print("****************************")
for name in sorted(favorite_laguage.keys()):
    print(name.title()+", thank you for taking the poll")

print("The following language have been mentioned:")
for language in favorite_laguage.values():
    print(language.title())
print("****************************")
print("The following language have been mentioned: ")
for language in set(favorite_laguage.values()):
    print(language.title())