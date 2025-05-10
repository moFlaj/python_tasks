gallons_used = int(input('Enter the gallons used (-1 to end): '))
miles_driven = int(input('Enter miles driven: '))
sum_miles = 0
sum_gallons = 0
while gallons_used != -1:
	sum_miles = sum_miles + miles_driven
	sum_gallons = sum_gallons + gallons_used
	miles_per_gallon = miles_driven//gallons_used
	print(miles_per_gallon)
	gallons_used = int(input('Enter the gallons used (-1 to end): '))
	miles_driven = int(input('Enter miles driven: '))

combined_mpg = sum_miles//sum_gallons
print(combined_mpg)
