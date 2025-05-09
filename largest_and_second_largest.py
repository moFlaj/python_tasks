largest = int(input('Enter number: '))
second_largest = largest
for number in range(9):
	numbers = int(input('Enter number: '))
	if numbers > largest:
		second_largest = largest
		largest = numbers
	elif numbers < largest:
		if numbers < second_largest:
			numbers = numbers;
		elif numbers > second_largest:
			second_largest = numbers;

print('Largest number is',largest)
print('Second largest number is',second_largest)
				
	
		






	
