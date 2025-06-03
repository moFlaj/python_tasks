import atmRunnerMod
import unittest
from decimal import Decimal, getcontext, ROUND_HALF_UP
getcontext().rounding = ROUND_HALF_UP


class TestAtm(unittest.TestCase):


	def testSetBalanceIsNotNegative(self):
		balance_input = 15000
		user_account = {'Account balance': None}
		actual = atmRunnerMod.set_balance(user_account, balance_input)
		expected = 'Your current balance is: 15000.00'
		self.assertEqual(actual, expected)

	def testSetBalanceDoesNotAcceptNegativeInput(self):
		balance_input = -15000
		user_account = {'Account balance': None}
		actual = atmRunnerMod.set_balance(user_account, balance_input)
		expected = 'Negative account balance'
		self.assertEqual(actual, expected)
		

	def testGetAccountBalanceReturnsAccountBalance(self):
		balance_input = 15000
		user_account = {'Account balance': None}
		atmRunnerMod.set_balance(user_account,balance_input)
		actual = atmRunnerMod.get_account_balance(user_account)
		expected = 15000
		self.assertEqual(actual, expected)

	def testWithdrawalAmmountCannotBeNegative(self):
		balance_input = 15000
		user_account = {'Account balance': None}
		user_history = list()
		atmRunnerMod.set_balance(user_account,balance_input)
		withdrawal_amt = -5000
		convert_to_dec = Decimal(str(withdrawal_amt))
		round_withdrawal = convert_to_dec.quantize(Decimal("0.01"))
		actual = atmRunnerMod.withdrawal(user_account,round_withdrawal, user_history)
		expected = 'Invalid amount'
		self.assertEqual(actual, expected)

	def testViewBalanceUpdatesAfterWithdrawal(self):
		balance_input = 15000
		user_account = {'Account balance': None}
		user_history = list()
		atmRunnerMod.set_balance(user_account,balance_input)
		withdrawal_amt = 5000
		convert_to_dec = Decimal(str(withdrawal_amt))
		round_withdrawal = convert_to_dec.quantize(Decimal("0.01"))
		atmRunnerMod.withdrawal(user_account,round_withdrawal, user_history)
		actual = atmRunnerMod.get_account_balance(user_account)
		expected = 9900.00
		self.assertEqual(actual, expected)

	def testTransactionHistoryUpdateAfterWithDrawal(self):
		balance_input = 15000
		user_account = {'Account balance': None}
		user_history = list()
		atmRunnerMod.set_balance(user_account,balance_input)
		withdrawal_amt = 5000
		convert_to_dec = Decimal(str(withdrawal_amt))
		round_withdrawal = convert_to_dec.quantize(Decimal("0.01"))
		atmRunnerMod.withdrawal(user_account,round_withdrawal, user_history)
		actual = user_history
		expected = [5000.00]
		self.assertEqual(actual, expected)