import numpy.random as random


class User:
	def __init__(self, l_size: int) -> None:
		self.l: int = l_size  # ilość przydzielonych bloków zasobów
		self.d: int = random.randint(low=1, high=10) * 250  # ilość odbieranych danych przez użytkownika

	def l_update(self, l_size: int):
		self.l = l_size

	def d_update(self):
		self.d = random.randint()
