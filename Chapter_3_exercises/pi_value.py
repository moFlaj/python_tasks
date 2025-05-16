counter = 1
count = 0
pi = 1
pi_values = 0
rounded_number = 0
approx = 2
true = True
count_one_four = 0
count_one_four_one = 0
count_one_four_one_five = 0
count_one_four_one_five_nine = 0

while true:

	pi = 4/counter

	if count % 2 == 0:
		pi_values = pi_values + pi
	else:
		pi_values = pi_values - pi

	rounded_number = round(pi_values, approx)

	if count_one_four == 0:
		if rounded_number == 3.14:
			count_one_four+=1
			print(f'Takes {count} terms to get 3.14')
			approx+=1
			print()
			
	if count_one_four_one == 0:
		if rounded_number == 3.141:
			count_one_four_one+=1
			print(f'Takes {count} terms to get 3.141')
			approx+=1
			print()

	if count_one_four_one_five == 0:
		if rounded_number == 3.1415:
			count_one_four_one_five+=1
			print(f'Takes {count} terms to get 3.1415')
			approx+=1
			print()
			

	if count_one_four_one_five_nine == 0:
		if rounded_number == 3.14159:
			count_one_four_one_five_nine +=1
			print(f'Takes {count} terms to get 3.14159')
			approx+=1
			true = False
			print()

	counter = counter + 2
	count = count + 1
	



	
    
