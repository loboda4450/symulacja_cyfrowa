from typing import Iterable
import numpy.random as random

import BTS


class Network:
	epsilon: float = 0.1  # prawodpodobienstwo przerwania transmisji
	k: int = 15  # ilość Resource Blocks
	s: int = 1  # czas co ile przydzielane są bloki zasobów RB
	l: int = 3  # ilość przypisywanych ResourceBlocks kolejnym użytkownikom jeżeli jest < 5 userów

	def __init__(self):
		self.bts: BTS = BTS.BTS(k_=self.k, s_=self.s, epsilon_=self.epsilon)
		print('started')