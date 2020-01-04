# 字符串拼接
first_name = "ada"
last_name = "lovelace"
full_name = first_name + " " + last_name
print("Hello, " + full_name.title() + "!")
# 制表符\t
# 换行符\n
# 可以先换行再制表
# 删除空白
# rstrip 删除后面的空白
# strip  删除前后的空白
# lstrip 删除前面的空白
# 列表就是由一系列按照特定顺序排列的元素组成用[]表示列表，用逗号分割其中的元素
car=['Audio','BMW','QQ']
print(car[-1]) #正数第一个数
print(car[0])  #倒数第一个数
motorcycles=['BMW','Audio']
motorcycles.append('suzuki') #向列表中添加元素
motorcycles.insert(0,'ducati')#在第一个位置添加元素
del motorcycles[0]           #删除第一个元素
popped_motorcycle = motorcycles.pop()
print(popped_motorcycle)
print(motorcycles)
print("==================================================================")
motorcycles = ['honda','yamaha','suzuki','Bmw','Lamborghini','ferrari']
first_owned = motorcycles.pop(0)
print('The first motorcycle I owned was a ' + first_owned.title() + '.')
# 利用pop删除元素(删除之后可以保存)
second_owned = motorcycles.pop(1)
print(motorcycles)
#根据值删除元素
motorcycles.remove('yamaha')
print(motorcycles)
too_expensive ='ferrari'
motorcycles.remove(too_expensive)
print(too_expensive)
print("==================================================================")
cars = ['honda','yamaha','suzuki','Bmw','Lamborghini','ferrari']
print('Here is a temp sort list')
print(sorted(cars)) #临时排序
print('here is original list')
print(cars)
cars.sort() # 永久排序
# print('Here is the final sort listr')
# print(cars)
print("==================================================================")
print('here is original list')
print(cars)
cars.reverse() # 反转列表元素排列顺序
print(cars)
print("==================================================================")
i = len(cars)
print(i)
print("==================================================================")