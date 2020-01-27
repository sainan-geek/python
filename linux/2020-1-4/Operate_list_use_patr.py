players = ['charles','martina','michael','florence','eli']
print(players[0:3]) #切片的使用 输出也是一个列表 包含前三名成员  从0开始加一
print(players[:5])  #没有指定第一个索引，python将自动从表头开始
print(players[2:])  #从第三个开始到最后一个
print(players[-3:]) #负数索引返回离列标末尾相应距离的元素
print("=====================遍历切片======================")
print("Here are the first three players on my team")
for player in players[0:3]:
	print(player.title())
print("=====================列表复制======================")
my_food = ['pizza','falafel','carrot cake']#falafel 沙拉三明治
friend_food = my_food[:]  #不能写成friend_food = my_food
my_food.append('cannoli')
friend_food.append('ice cream')
print("My favorite food are:")
print(my_food)
print("\nMy friend favorite food are:")
print(friend_food)
print("=====================practice======================")
print("The first three items in the list are :")
print(players[0:3])
print("Three items from the middle of the list are:")
print(players[1:4])
print("The last three items in the list are :")
print(players[-3:])
