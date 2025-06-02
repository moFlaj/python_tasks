import random
#startTime = new Date()
firstNumber = 0
secondNumber= 0
noOfTries = 0
runProgram = 0
totalScore = 0

while runProgram < 10:
	firstNumber = random.randint(0,100)
	secondNumber = random.randint(0,100)

	if firstNumber > secondNumber:
		runProgram+=1
		if runProgram == 1:
			print(f"Start time is")
		while True:
			print(f"What will be the result of this operation: {firstNumber} - {secondNumber}")
			answer = int(input("Answer: "))
		
			if answer != (firstNumber - secondNumber):
				noOfTries+=1
				print("Wrong answer. You have one more try for this question.")
				if noOfTries == 2:
					guessAnswer = False
					noOfTries = 0
					break

			
				else:
					continue			

			elif answer == (firstNumber - secondNumber):
				totalScore+=1
				break


	else:
		continue


print(f"Your total score is {totalScore}.")
