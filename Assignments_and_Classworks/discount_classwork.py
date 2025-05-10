
discount_amount = 0
total_spend = int(input('Enter total spend: '))

if total_spend > 0:
	if	total_spend > 999:
		if	total_spend > 1000 and total_spend < 10000:
			discount_amount = total_spend * (15/100)
			final_amount = total_spend - discount_amount
			
		elif	total_spend > 10000 and total_spend < 50000:
			discount_amount = total_spend * (10/100)
			final_amount = total_spend - discount_amount
			
		elif	total_spend > 50000:
			discount_amount = total_spend * (20/100)
			final_amount = total_spend - discount_amount
		print(f'Total cost of goods purchased is {final_amount:,.2f}.')

	elif  total_spend <= 999 and total_spend > 0:
			print('No discount')

else:
	print('Invalid Amount.')
			
