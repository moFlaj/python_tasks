principal = int(input('Enter the principal amount: '))
annual_rate = int(input('Enter the annual interest: '))
duration_years = int(input('Enter the duration in years: '))

monthly_rate = (annual_rate/100)/12
duration_months = duration_years * 12
monthly_payment = principal* ((monthly_rate * ((1 + monthly_rate)**duration_months))/(((1 + monthly_rate)**duration_months)-1))

print('Your monthly payment is',monthly_payment)
