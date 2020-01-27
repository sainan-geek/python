# 字典
alien_0 = {'color':'green','point':5}
print(alien_0['color'])

print('====================================================')
#添加

alien_0['x_position'] = 24
alien_0['y_position'] = 39
print(alien_0)

#元素可以被重新赋值

alien_0['color'] = 'red'
print(alien_0)
print('====================================================')

#一个小例子

alien_1 = {'x_position':0,'y_position':25,'speed':'medium'}
print("Original x-position:"+ str(alien_1['x_position']))

# Move The alien to the Right 
# Determine how far to move the alien based on its current speed

if alien_1['speed']=='slow':
    x_increment = 1
elif alien_1['speed']=='medium' :
    x_increment = 2
else:
    x_increment = 3

alien_1['x_position'] = alien_1['x_position']+x_increment

print("New x_position:" + str(alien_1['x_position']))

#找错误如果当行标错找不到优先找上一行

favorite_language = {
    'jen':'python',
    'sarah':'c',
    'edward':'ruby',
    'phil':'python'
}
print("Sarah's favorite language is " +favorite_language['sarah'].title()+".");