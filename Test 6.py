class Bank_Account:
	def __init__(self):
		self.bal=0

	def deposit(self):
		amt=float(input("Enter Deposited Amt: "))
		self.bal += amt
		print("\n Amount Deposited:",amt)

	def withdraw(self):
		amt = float(input("Enter Withdrawn Amt: "))
		if self.bal>=amt:
			self.bal-=amt
			print("\n You Withdrew:", amt)
		else:
			print("\n Insufficient balance ")

	def display(self):
		print("\n Net Available Balance=",self.bal)

s = Bank_Account()
s.deposit()
s.withdraw()
s.display()
