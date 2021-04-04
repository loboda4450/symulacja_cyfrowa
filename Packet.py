from numpy.random import random_sample, randint


class Packet:
	def __init__(self, _epsilon: float, _size: int, _log: bool):
		self.epsilon: float = _epsilon  # prawdopodobieństwo wysłania pakietu
		self.is_sent: bool = (random_sample() >= _epsilon)  # czy pakiet zostanie wysłany
		self.packet_size: int = _size
		self.log: bool = _log
