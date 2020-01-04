print('==========4-3==========')
numbers = range(1,21)
for number in numbers:
	print(number)
print('==========4-4==========')
numbers_list = list(range(1,100001))
#for num in numbers_list:
	#print(num)

print('==========4-5==========')
print('==========min==========')
print(min(numbers_list))
print('==========max==========')
print(max(numbers_list))
print('==========sum==========')
print(sum(numbers_list))
print('==========4-6==========')
numbers_list = list(range(1,21,2))
print(numbers_list)
print('==========4-7==========')
squares=[]
for value in range(3,31):
	square = value*3
	squares.append(square)
print(squares)
print('==========4-8==========')
squares_1=[]
for value in range(1,11):
	square_1=value**3
	squares_1.append(square_1)

print(squares_1)

square_2 = [value**3 for value in range(1,11)]
print(square_2)
