grade = int(input('Enter grade: '))
largest = grade
smallest = grade
sum = 0
product = 1
grade_counter = 1

for no_of_grades in range(4):
	++grade_counter 
	sum+=grade
	product*=grade
	if grade > largest:
		largest = grade
	if grade < smallest:
		smallest = grade 
	grade = int(input('Enter grade or -1 to end: '))


if grade_counter != 0:
	average = sum/grade_counter 
	print(f'Average is {average:.2f}')
	print(f'Sum is is {sum}')
	print(f'Product is {product}')
	print(f'Largest is {largest}')
	print(f'Smallest is {smallest}')
	
else:
    print('No grades were entered')


	