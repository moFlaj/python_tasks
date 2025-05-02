number = int(input('Enter five digit integer: '))
if number < 10000:
	print('Invalid input')

if number > 99999:
	print('Invalid input')

if number >= 10000: 
	if number <= 99999:
		first_digit = number // 10000
		number = number % 10000
		second_digit = number // 1000
		number = number % 1000
		third_digit = number // 100
		number = number % 100
		fourth_digit = number // 10
		number = number % 10
		fifth_digit = number // 1
		
		print(first_digit,second_digit,third_digit,fourth_digit,fifth_digit)
		
	

