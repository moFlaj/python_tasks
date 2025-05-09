number = int(input('Enter five digit number: '))
if number > 9999 and number < 100000:
	divisor = 10000
	for numbers in range(5):
			if number > 9999 and number < 100000:
				first_digit = int(number // divisor)
			elif number > 999 and number < 10000:
				second_digit = int(number // divisor)
			elif number > 99 and number < 1000:
				third_digit = int(number // divisor)
			elif number > 9 and number < 100:
				fourth_digit = int(number // divisor)
			elif number >= 0 and number < 10:
				fifth_digit = int(number // divisor)
			number = number % divisor
			divisor = divisor/10
			
	if first_digit == fifth_digit and second_digit == fourth_digit:
		print('Number is a palindrome.')
	else:
		print('Number is not a palindrome.')
		
			
			
else:
	print('Enter valid input.')
