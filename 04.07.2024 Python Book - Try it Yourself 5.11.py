numbers = [1,5,6,4,3,2,7,9,8]
numbers.sort()

for num in numbers:
	if num == 1:
		print(str(num)+"st")
	elif num == 2:
		print(str(num)+"nd")
	elif num == 3:
		print(str(num)+"rd")
	else:
		print(str(num)+"th")
