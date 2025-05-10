smallest = input('Enter number: ');
numberTwo = input('Enter number: ');
numberThree = input('Enter number: ');



if(numberTwo < smallest and numberTwo < numberThree and numberThree < smallest):
	print(numberTwo,numberThree,smallest)
elif(numberTwo < smallest and numberTwo < numberThree and numberThree > smallest):
	print(numberTwo,smallest,numberThree)
elif(numberTwo < smallest and numberTwo > numberThree and numberThree < smallest):
	print(numberThree,numberTwo,smallest)
elif(numberTwo > smallest and numberTwo > numberThree and numberThree < smallest):
	print(numberThree,smallest,numberTwo)
elif(smallest < numberTwo and smallest < numberThree and numberTwo < numberThree):
	print(smallest,numberTwo,numberThree)
elif(smallest < numberTwo and smallest < numberThree and numberTwo > numberThree):
	print(smallest,numberThree,numberTwo)

	