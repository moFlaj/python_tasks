number = int(input('Enter five digit number: '))
if number > 9999 and number < 100000:
	divisor = 10000
	for numbers in range(5):
			digit = int(number // divisor)
			number = number % divisor
			divisor = divisor/10
			print(digit, end = ' ')
else:
	print('Enter valid input.')
			
		
		