import logging
from time import sleep

import numpy.random as random
from typing import List

import User
import Network
from ResourceBlock import ResourceBlock


class BTS:
	def __init__(self, k_: int, s_: int, epsilon_: float, clock_: int) -> None:
		self.user_list: List[User] = list()
		self.k: int = k_  # ilość Resource Blocks
		self.rb_list: List[ResourceBlock] = [ResourceBlock() for _ in range(self.k)]
		self.s: int = s_  # czas co ile przydzielane są bloki zasobów RB
		self.epsilon: float = epsilon_
		self.tau: float = random.exponential(
			scale=1 / 10)  # odstęp czasowy między zmianą warunków propagacji dla każdego usera
		self.t: float = random.exponential(scale=1 / 10)  # czas co ile pojawiają się nowi userzy
		self.clock: int = clock_  # zegar BTSa
		self.cycles_done: int = 0  # wykonane cykle zegarowe przez BTS.

		logging.getLogger(__name__).info(msg='Created BTS')

		while self.add_user(l=Network.Network.l) < 10:
			sleep(self.t)

	def add_user(self, l: int):
		if len(self.user_list) * l < self.k:
			self.user_list.append(User.User(resource_blocks=self.rb_list[len(self.user_list): len(self.user_list) + l]))
		else:
			self.user_list.append(User.User(resource_blocks=list()))

		logging.getLogger(__name__).info(msg='Added BTS user')
		return len(self.user_list)

	def remove_user(self, user: User):
		del user
		user = None
		logging.getLogger(__name__).info(msg='Removed BTS user')

	def t_update(self):
		self.t = random.exponential(scale=1 / 50)
		logging.getLogger(__name__).info(msg=f'Updated time t = {self.t}')

	def t_expire(self):
		logging.getLogger(__name__).info(msg='Time t expired, adding new user and generating new time t')
		self.add_user(l=Network.Network.l) if len(self.user_list) * Network.Network.l < self.k else self.add_user(l=0)
		self.t_update()

	def s_expire(self):
		logging.getLogger(__name__).info(msg='Time s expired, updating users ResourceBlocks count')
		for num, user in enumerate(self.user_list):
			if num * Network.Network.l <= self.k:
				user.rb_list_update()
			else:
				pass

	def tau_expire(self):
		logging.getLogger(__name__).info(msg='Time tau expired, updating ResourceBlocks')
		for rb in self.rb_list:
			rb.update_throughput()
