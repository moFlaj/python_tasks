no_of_students = int(input('Enter number of students: '))
max_name = input('Enter student name: ')
max_score = int(input('Enter student score: '))
names = max_name + ', '
count = 0
for score in range(1, no_of_students):
	student_name = input('Enter student name: ')
	student_score = int(input('Enter student score: '))

	if student_score == max_score:
		count += 1
		names =  names + student_name + ', '
				
	if student_score > max_score:
		max_score = student_score
		max_name = student_name
		count = 0
		names = max_name + ', '

if count == 0:
	print(f'Highest score is {max_score}.', end = ' ')
	print(f'{max_name} scored the highest.')

elif count > 0:
	print(f'Highest score is {max_score}.', end = ' ') 
	print(f'{names} scored the highest.')

			
