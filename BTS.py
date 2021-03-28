from time import sleep

import numpy.random as random
import User
import Network
import ResourceBlock


class BTS:
	def __init__(self, k_: int, s_: int, epsilon_: float) -> None:
		self.user_list: list = list()
		self.k: int = k_  # ilość Resource Blocks
		self.rb_list: list = [ResourceBlock.ResourceBlock() for _ in range(self.k)]
		self.s: int = s_  # czas co ile przydzielane są bloki zasobów RB
		self.epsilon: float = epsilon_
		self.tau: float = random.exponential(scale=1 / 10)  # odstęp czasowy między zmianą warunków propagacji dla każdego usera
		self.t: float = random.exponential(scale=1/10)  # czas co ile pojawiają się nowi userzy

		while self.add_user(l=Network.Network.l) < 4:
			sleep(self.t)

	def add_user(self, l: int):
		self.user_list.append(User.User(l_size=l))
		print('Added new user lol')
		return len(self.user_list) - 1

	def t_update(self):
		self.t = random.exponential(scale=1 / 50)

	def t_expire(self):
		self.add_user(l=Network.Network.l) if len(self.user_list)*3 < self.k else self.add_user(l=0)
		self.t_update()

	def s_expire(self):
		for num, user in enumerate(self.user_list):
			if num * Network.Network.l <= self.k:
				user.l_update(l_size=Network.Network.l)
			else:
				user.l_update(l_size=0)

	def tau_expire(self):
		[user.rk_update() for user in self.user_list]

