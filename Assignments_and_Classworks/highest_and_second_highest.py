no_of_students = int(input('Enter number of students: '))
max_name = input('Enter student name: ')
max_score = int(input('Enter student score: '))
second_max_name = max_name
second_max_score = max_score
names_max = max_name + ', '
names_second = ''
count = 1
count_second = 1


for score in range(2, no_of_students + 1):

	student_name = input('Enter student name: ')
	student_score = int(input('Enter student score: '))

		
	if student_score < second_max_score and second_max_score == max_score:
		second_max_score = student_score
		second_max_name = student_name
		names_second = second_max_name + ', '


	elif student_score == max_score:
		count += 1
		names_max =  names_max + student_name + ', '


	elif student_score > max_score:
		second_max_score = max_score
		second_max_name = max_name
		count_second = 1
		names_second = second_max_name + ', '
		max_score = student_score
		max_name = student_name
		count = 1
		names_max = max_name + ', '

	elif student_score < max_score and second_max_score != max_score:

		if student_score == second_max_score:
			count_second+=1
			names_second = names_second + student_name + ', '
			
		elif student_score < second_max_score:
			student_score = student_score
			student_name = student_name

		elif student_score > second_max_score:
			second_max_score = student_score
			second_max_name = student_name
			names_second = second_max_name + ', '
			count_second = 1
			
if count < no_of_students:

	if count == 0:
		print(f'Highest score is {max_score}.', end = ' ')
		print(f'{max_name} scored the highest.')

	elif count > 0:
		print(f'Highest score is {max_score}.', end = ' ') 
		print(f'{names_max} are the students with the highest scores.')


	if count_second == 0:
		print(f'Second highest score is {second_max_score}.', end = ' ')
		print(f'{second_max_name} is the student with the second highest score.')

	elif count_second > 0:
		print(f'Second highest score is {second_max_score}.', end = ' ') 
		print(f'{names_second} are the students with the second highest scores.')

if count == no_of_students:
	print(f'Highest score is {max_score}.', end = ' ')
	print(f'All students scored the same.')
	

	