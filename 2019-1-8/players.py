playres=['charles','martina','minchael','florence','eli']
print (playres[1:4])
#切片
#执行结果 (截取了1 2 3 三个元素)
#['martina', 'minchael', 'florence']
print(playres[:4])
#默认从头开始，同理到结尾
#['charles', 'martina', 'minchael', 'florence']
print(playres[-3:])
#['minchael', 'florence', 'eli']
for playre in playres[:3]:
    print(playre.title())