userAge = int(input('Enter age in years: '))
if userAge > 0:
	maxHeart = 220 - userAge

	targetHeartRateMin = int(maxHeart * 0.5)
	targetHeartRateMax = int(maxHeart * 0.85)
	print('Your maximum heart rate is',maxHeart,'bpm')
	print('Your target heart rate zone ranges from',targetHeartRateMin,'bpm and',targetHeartRateMax, 'bpm.')
else:
	print('Enter valid input.')
