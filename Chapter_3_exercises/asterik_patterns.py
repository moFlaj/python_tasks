count = 1
while count <= 10:
	for counter in range(0,count):
		print('*', end = ' ')
	count+=1
	print()

print()

count = 10
while count > 0:
	for counter in range(0,count):
		print('*', end = ' ')
	count-=1
	print()

print()

count = 10
space_count = 0
while count > 0:
	if count <= 9:
		for counterOne in range(0,space_count):
			print(' ', end = ' ')
	for counter in range(0,count):
		print('*', end = ' ')
	count-=1
	space_count+=1
	print()

print()

count = 1
space_count = 9
while count <= 10:
	if count >= 1:
		for counterOne in range(0,space_count):
			print(' ', end = ' ')
	for counter in range(0,count):
		print('*', end = ' ')
	count+=1
	space_count-=1
	print()







