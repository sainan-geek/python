dimensions = (200,50) #定义元组圆括号
print(dimensions[0])  
print(dimensions[1])
# dimensions[0]=250; 不能修改元组中某个元素的值
# 可以像列表一样遍历
# magicians = ['alice', 'david', 'carolina']
# for magician in magicians:
#	print(magician)
for dimension in dimensions:
	print(dimension)

dimensions = ('apple','orange','grape','watermellon')
for dimension in dimensions:
	print(dimension)
dimensions = ('apple','orange','grape','watermellon','wine','redbull')
for dimension in dimensions:
	print(dimension)
