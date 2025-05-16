number = int(input('Enter an integer between 1 and 10000: '))

if number > 1 and number < 10000:
	sum = 0
	while number != 0:
		digits = number % 10
		sum += digits
		number = number // 10

	print(f'Sum of digits of integer entered is {sum}.')

else:
	print('Enter valid input.')


		
		
