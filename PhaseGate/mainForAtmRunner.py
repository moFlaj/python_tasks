
user_history = []
user_account = {'Account balance': None}

atm_runner = True
print('Welcome to Semicolon bank')
while atm_runner:
	balance_input = input('Enter account balance: N')
	print(set_balance(user_account, balance_input))
	if get_account_balance(user_account) >= 0:
		option_menu = True
		while option_menu:
			options = input('1. Withdrawal	2. View all withdrawals: ')
			match options:
				case "1":
					withdrawalLoop = True
					while withdrawalLoop:
						withdrawal_amt = input('Enter withdrawal amount in multiples of N500 or N1000: N')
						convert_to_dec = Decimal(str(withdrawal_amt))
						round_withdrawal = convert_to_dec.quantize(Decimal("0.01"))
						print(withdrawal(user_account, round_withdrawal, user_history))
						another_transaction = True
						while another_transaction:
							response = input("""Do you want to make another withdrawal? 
Enter 1 for Yes, 2 to return to main menu  or 0 for to remove atm: """
)						
							match response:
								case "0": 
									withdrawalLoop = False
									atm_runner = False
									another_transaction = False
									option_menu = False
									continue
								case "1":
									another_transaction = False
									continue
								case "2":
									withdrawalLoop = False
									another_transaction = False
									continue
								case _:
									print("Invalid input")
				case "2":
					view_transactions(user_history)
					return_or_end = input('Press 0 to remove card or 1 to return to main menu: ')
					match return_or_end:
						case "0":
							option_menu = False
							atm_runner = False
						case "1":
							continue
						case _:
							print("Invalid input")
		
				case _:
					print("Invalid input")
				
				
	else:
		print('Enter valid account balance')