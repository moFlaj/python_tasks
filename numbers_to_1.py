number = int(input('Enter number: '))
true = True
false = False

while true:


	if number > 1:
		print(number)
		number = number - 1
		
	if(number == 1):
		print('Blast off!')
		while True:
			number = int(input('Enter number: '))
			if number >= 0:
				true = false
				break
			elif number < 1:
				continue
	
		

