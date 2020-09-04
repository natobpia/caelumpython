class Conta:

	def __init__(self, number, holder, balance, limit):
		self.number = number
		self.holder = holder
		self.balance = balance
		self.limit = limit

	def deposit(self, value):
		self.balance += value

	def draw(self, value):
		if(self.balance < value):
			return False
		else:
			self.balance -= value
			return True

	def extract(self):
		print("Número: {} Saldo: {}".format(self.number, self.balance))

	def transfer_to(self, destiny,value):
		withdrew = self.draw(value)
		if(withdrew == False):
			return False
		else:
			destiny.deposit(value)
			return True