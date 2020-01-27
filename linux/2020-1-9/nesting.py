#列表:由一系列按特定顺序排列的元素组成 bicycle = ['trek']
#字典:alien_0={'color':'green'}
alien_0 = {'color':'green','points':5}
alien_1 = {'color':'yellow','points':10}
alien_2 = {'color':'red','points':15}

aliens = [alien_0,alien_1,alien_2]

for alien in aliens:
    print(alien)

print("***********************************************")
aliens=[]
for alien_number in range(30):  #range()创建一个整数列表用在for循环中 range(star,stop[,step])  range(5)等价于rang(0,5)等价于(0,5,1)
    new_alien = {'color':'yellow','point':5,'speed':'slow'}
    aliens.append(new_alien)
for alien in aliens[:5]:
    print(alien)
print(".......")

print("Total number of aliens "+ str(len(aliens)))

for alien in aliens[0:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['point'] = 10
        alien['speed'] = 'slow'
    elif alien['color'] == 'yellow':
        alien['color'] = 'red'
        alien['point'] = 15
        alien['speed'] = 'faster'
for alien in aliens[0:8]:
    print(alien)
print(".....")