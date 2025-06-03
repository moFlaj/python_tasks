from decimal import Decimal, getcontext, ROUND_HALF_UP
getcontext().rounding = ROUND_HALF_UP


def set_balance(customer_dict, balance_input):
	message = ''
	try:
		amount_to_dec = Decimal(str(balance_input))
		round_up_amount = amount_to_dec.quantize(Decimal("0.01"))
		if(round_up_amount >= 0):
			customer_dict['Account balance'] = round_up_amount
			message = 'Your current balance is: ' + str(round_up_amount)
		else:
			raise ValueError("Negative account balance")
	except ValueError as e:
			message = e.args[0]
	return message



def get_account_balance(customer_dict):
	return customer_dict['Account balance']	


def withdrawal(customer_dict, amount, transaction_list):
	message = ''
	try:
		if(amount > 0 and amount % 500 == 0):
			try:
				if(amount < customer_dict['Account balance'] and (customer_dict['Account balance'] - amount) - 100 >= 100):
					balance_update = (customer_dict['Account balance'] - amount) - 100
					transaction_history(transaction_list, amount)
					customer_dict['Account balance'] = balance_update.quantize(Decimal("0.01"))
					message = 'Transaction successful' + '\n' + 'Withdrawal amount: '
					message = message + str(amount) + '\n' + 'Withdrawal fee: N100' + '\n'
					message = message + 'Remaining balance: ' + str(get_account_balance(customer_dict))


				else:
					raise ValueError('Insufficient funds')
			except ValueError as e:
				message = e.args[0]
		else:
			raise ValueError("Invalid amount")
	except ValueError as funds:
		message = funds.args[0]

	return message

def transaction_history(transaction_list, withdrawal_amount):
	transaction_list.append(withdrawal_amount)
	
def view_transactions(transaction_list):
	if len(transaction_list) > 0:
		number = 1
		for index in range(len(transaction_list)):
			print(str(number) + '.', 'N'+ str(transaction_list[index]))
			number += 1
	else:
		print('No past transactions.')


#Main






		

	

	




	
		
