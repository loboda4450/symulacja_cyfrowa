from numpy.random import random_sample, randint
import logging


class Packet:
	def __init__(self, _epsilon: float, _size: int, _log: logging):
		self.epsilon: float = _epsilon  # prawdopodobieństwo wysłania pakietu
		self.is_sent: bool = True  # czy pakiet zostanie wysłany, True by default
		self.packet_size: int = _size
		self.log: logging.Logger = _log.getChild(__name__)

		self.update_is_sent()

	def update_is_sent(self) -> None:
		self.is_sent = random_sample() >= self.epsilon
