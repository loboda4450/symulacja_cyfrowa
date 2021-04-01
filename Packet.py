from numpy.random import random_sample


class Packet:
	def __init__(self, _epsilon: float, _log: bool):
		self.epsilon: float = _epsilon  # prawdopodobieństwo wysłania pakietu
		self.is_sent: bool = (round(random_sample(), 1) == _epsilon)  # czy pakiet zostanie wysłany
		self.log: bool = _log