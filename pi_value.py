counter = 3
pi_value = 4
sum_pi = 0
count = 2

while True:

	pi = 4/counter
	if count % 2 == 0:
		sum_pi = sum_pi + pi
	else:
		sum_pi = sum_pi - pi

	pi_values = pi_value - sum_pi
	print(f'{pi_values:.5f}')
	if pi == 3.14159:
		break
	counter += 2
	count = count+1

    