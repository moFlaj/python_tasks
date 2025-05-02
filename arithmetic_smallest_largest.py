firstInt = int(input('Enter first number: '))
secondInt = int(input('Enter second number: '))
thirdInt = int(input('Enter third number: '))

sum = firstInt + secondInt + thirdInt
average = sum/3
smallest = firstInt
largest = firstInt

if secondInt < smallest:
	smallest = secondInt
if thirdInt < smallest:
	smallest = thirdInt

if secondInt > largest:
	largest = secondInt
if thirdInt > largest:
	largest = thirdInt

print('Sum of the three integers is', sum,'\n''Average of the three numbers is', average,'\n''The smallest number of the three is', smallest,'\n''The largest of the three is', largest)


