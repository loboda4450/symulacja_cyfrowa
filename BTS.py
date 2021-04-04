import logging
import numpy.random as random
from typing import List
from ResourceBlock import ResourceBlock
from User import User


class BTS:
	def __init__(self, k_: int, s_: int, epsilon_: float, clock_: int, _log: logging):
		self.log: logging = _log.getChild(__name__)
		self.user_list: List[User] = [User(_log=self.log) for _ in range(10)]
		self.k: int = k_  # ilość Resource Blocks
		self.rb_list: List[ResourceBlock] = [ResourceBlock(_log=self.log) for _ in range(self.k)]
		self.s: int = s_  # czas co ile przydzielane są bloki zasobów RB
		self.epsilon: float = epsilon_  # prawdopodobienstwo, że transmisja się nie uda
		self.tau: float = random.exponential(scale=1 / 10)  # odstęp czasowy między zmianą warunków propagacji dla każdego usera
		self.t: float = random.exponential(scale=1 / 10)  # czas co ile pojawiają się nowi userzy
		self.clock: int = clock_  # zegar BTSa
		self.cycles_done: int = 0  # wykonane cykle zegarowe przez BTS.

		self.log.info(msg='Created Base Transmitting Station')

	def add_user(self):
		self.user_list.append(User(_log=self.log))

	def remove_user(self, user: User):
		self.user_list.remove(user)
