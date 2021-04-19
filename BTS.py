import logging
import numpy.random as random
from typing import List
from ResourceBlock import ResourceBlock
from User import User


class BTS:
	def __init__(self, k_: int, s_: int, epsilon_: float, clock_: int, _log: logging):
		self.log: logging.Logger = _log.getChild(__name__)
		self.k: int = k_  # ilość Resource Blocks
		self.k_max: int = 3  # ilość ResourceBlocków do przydzielenie maksymalnie
		self.s: int = 10  # s_  # czas co ile przydzielane są bloki zasobów RB
		self.epsilon: float = epsilon_  # prawdopodobienstwo, że transmisja się nie uda
		self.tau: float = 10  # random.exponential(scale=1 / 10)  # odstęp czasowy między zmianą warunków propagacji dla każdego usera
		self.t: float = 5  # random.exponential(scale=1 / 10)  # czas co ile pojawiają się nowi userzy
		self.clock: int = clock_  # zegar BTSa (1 cykl = 1ms)
		self.cycles_done: int = 0  # wykonane cykle zegarowe przez BTS.
		self.taken_rb_count: int = 0  # ilość zajętych ResourceBlocków
		# self.rb_list: List[ResourceBlock] = [ResourceBlock(_log=self.log, _epsilon=self.epsilon) for _ in range(self.k)]
		self.user_list: List[User] = [User(_log=self.log, _rb=[ResourceBlock(_log=self.log, _epsilon=self.epsilon)]) for _ in range(self.k)]

		self.log.log(msg='Created Base Transmitting Station', level=1)

	def run(self, step_by_step: bool):
		while True:
			self.step()

			if step_by_step:
				if input('Press "Enter" to continue, ":q!" then "Enter" to exit simulation...\n') == ':q!':
					exit(0)

	def step(self):
		for user in self.user_list:
			if user.d > 0:
				user.send_packet()
				if user.d <= 0:
					self.remove_user(user)

		if not self.cycles_done % self.t:
			self.add_user()
			print(len(self.user_list))
			self.log.log(msg='Added user', level=1)

		if not self.cycles_done % self.tau:
			self.update_users_throughput()
			self.log.log(msg='Updated users propagation conditions', level=1)

		if not self.cycles_done % self.s:
			self.redistribute_resource_blocks()
			self.log.log(msg='Updated users throughput and resource blocks', level=1)

		self.cycles_done += self.clock

	def add_user(self):
		rb = list()
		for i in range(self.k):
			if i <= self.k_max and self.taken_rb_count < self.k:
				rb.append(ResourceBlock(_log=self.log, _epsilon=self.epsilon))
				self.taken_rb_count += 1

		self.user_list.append(User(_log=self.log, _rb=rb))

	# self.log.log(msg='Added user to BTS!', level=1)

	def remove_user(self, user: User):
		self.user_list.remove(user)

	# self.log.log(msg='Removed user!', level=1)

	def update_users_throughput(self):  # Update throughput of existing ResourceBlocks
		for user in self.user_list:
			user.update_user_existing_rbs()

	def redistribute_resource_blocks(self):  # Algorithm defined by A in exercise
		pass
