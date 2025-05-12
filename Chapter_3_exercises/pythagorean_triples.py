
for hyp in range(1,21):
	
	for number in range(1,21):

		for opp in range(1, 21):
		
			if number ** 2 + opp ** 2 == hyp ** 2:
				print(number,opp,hyp)
		