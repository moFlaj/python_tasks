

def sum_digitsOf_integer(number):
	if number > 1 and number < 10000:
		sum = 0
		while number != 0:
			digits = number % 10
			sum += digits
			number = number // 10
		return sum


	else:
		print('Enter valid input.')


number = int(input('Enter an integer between 1 and 10000: '))

print(sum_digitsOf_integer(number))