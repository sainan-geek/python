# alien_0 = {'color':'green','point':5}
# alien_1 = {'color':'yellow','point':10}
# alien_2 = {'color':'red','point':15}

# aliens = [alien_0,alien_1,alien_2]
# for alien in aliens:
#     print(alien)

aliens = []

for alien_number in range(0,30):
    new_alien = {'color':'green','point':5,'speed':'slow'}
    aliens.append(new_alien)    # append() 方法用于在列表末尾添加新的对象


print("===========================================================================")
for alien in aliens[0:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['point'] = 10
    elif alien['color'] == 'yellow':
        aline['color'] = 'red'
        alien['speed'] = 'fast'
        alien['point'] = 15

for alien in aliens[0:5]:
    print(alien)

print("Total number of aliens: "+ str(len(aliens)))

