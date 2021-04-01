import logging
from typing import List
from ResourceBlock import ResourceBlock
from Packet import Packet

import numpy.random as random


class User:
	def __init__(self, _log: bool):
		self.d: int = random.randint(low=1, high=10) * 250  # [b] losowa (rozkład jednostajny) liczba odbieranych danych przez użytkownika
		self.user_rb_list: List[ResourceBlock] = list()  # lista przydzielonych bloków zasobów użytkownikowi
		self.packet_list: List[Packet] = list()  # lista pakietów przypisanych do użytkownika
		self.prev_d: List[ResourceBlock] = list()  # lista poprzednio przydzielonych bloków zasobów (używana do obliczania sum_d)
		self.sum_d: int = 0  # nie ma sensu z tego wyciągać średniej, jeżeli numa >= numb, to numa/5 >= numb/5
		self.log: bool = _log

		if self.log:
			logging.getLogger(__name__).info(msg=f'Created user: {self.d, self.user_rb_list, self.sum_d}')

	def update_d(self) -> int:
		return self.d

	def append_to_rb_list(self, element: ResourceBlock):
		self.user_rb_list.append(element)
		if self.log:
			logging.getLogger(__name__).info(msg=f"Appended ResourceBlock to user's rb_list")

	def update_rb_list(self, swap: List[ResourceBlock]) -> List[ResourceBlock]:
		self.user_rb_list = swap
		if self.log:
			logging.getLogger(__name__).info(msg=f"'Updated ResourceBlock to user's rb_list'")
		return self.user_rb_list

	def update_prev_d(self) -> List[ResourceBlock]:
		self.prev_d = self.prev_d[1:]
		# if self.log:
		# 	logging.getLogger(__name__).info(msg=f"Updated user's previously received data.")
		return self.prev_d

	def update_sum_d(self) -> int:
		# if self.log:
		# 	logging.getLogger(__name__).info(msg=f"Updated user's d-sum.")
		return self.sum_d
