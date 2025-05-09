password = input('Enter password: ')

if len(password) < 8:
	print('Very weak')
elif len(password) == 8:
	print('Weak')
elif len(password) > 8 and len(password) < 16:
	print('Strong')
else: 
	print('Very Strong')




