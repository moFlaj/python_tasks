count = 1
count_pattern_one = 1
count_pattern_two = 10
count_pattern_three = 10
space_count_three = 0
space_count_four = 9
count_pattern_four = 1
while count <= 10:
	for counter in range(0,count_pattern_one):
		print('*', end = '')

	print(end = '        ')
	for counter in range(0,count_pattern_two):
		print('*', end = '')

	print(end = '        ')
	for counter in range(0,1):
		if count_pattern_three <= 9:
			for counterOne in range(0,space_count_three):
				print('', end = '')
		for counter in range(0,count_pattern_three):
			print('*', end = '')

	print(end = '        ')
	for counter in range(0,1):
		if count_pattern_four >= 1:
			for counterOne in range(0,space_count_four):
				print('', end = '')
		for counter in range(0,count_pattern_four):
			print('*', end = '')
	

	print()

	count = count + 1
	count_pattern_one+=1
	count_pattern_two-=1
	count_pattern_three-=1
	space_count_three+=1
	space_count_four-=1
	count_pattern_four+=1


