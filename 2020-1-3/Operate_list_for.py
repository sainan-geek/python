magicians = ['alice','david','carolian']
for magician in magicians:   #    for magician in magicians  SyntaxError: invalid syntax(没有冒号)

	print(magician.title() + ",that was a great trick!") #IndentationError: expected an indented block(没有找到期望缩进的代码)
	print("I can't wait to see your next trick, " + magician.title() + ".\n")
print("Thank you everyone.That was a great magic show")#没有缩进只执行了一次

message = 'Hello Python World'
print(message) #IndentationError: unexpected indent(不在预期内的缩进)
#创建数值列表
print('创建数值列表')
for value in range(1,5): #生成数值1-4不包含5
	print(value)

number = list(range(1,5))   #创建了一个数值列表
print(number)

#打印1-10的偶数
print('打印1-10的偶数')
even_number = list(range(2,11,2)) #从2数不断加2直到11
print(even_number)
print('打印1-10的奇数')
odd_number = list(range(1,10,2))
print(odd_number)
print('打印1-10的平方')
squares=[]
for value in range(1,11):
	squares.append(value**2)	#square = value**2
								#squares.append(square)
print(squares)

number = list(range(1,101))
print('=============min================\n')
print(min(number))
print('=============max================\n')
print(max(number))
print('=============sum================\n')
print(sum(number))
print('列表解析')
squares =[value**2 for value in range(1,11)]
print(squares)
