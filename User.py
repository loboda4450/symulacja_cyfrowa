import logging
from typing import List
from ResourceBlock import ResourceBlock
from Packet import Packet

from numpy.random import randint


class User:
	def __init__(self, _log: logging):
		self.log: logging = _log.getChild(__name__)
		self.d: int = randint(low=1, high=10) * 250  # [b] losowa (rozkład jednostajny) liczba odbieranych danych przez użytkownika
		self.user_rb_list: List[ResourceBlock] = [ResourceBlock(_log=self.log) for _ in range(3)]  # lista przydzielonych bloków zasobów użytkownikowi
		self.packet_list: List[Packet] = self.generate_packets()  # lista pakietów przypisanych do użytkownika
		self.prev_d: List[ResourceBlock] = list()  # lista poprzednio przydzielonych bloków zasobów (używana do obliczania sum_d)
		self.sum_d: int = 0  # nie ma sensu z tego wyciągać średniej, jeżeli numa >= numb, to numa/5 >= numb/5

		self.log.info(msg=f'Created user: {self.d, self.user_rb_list, self.sum_d}')

	def generate_packets(self):
		remaining = self.d
		pckt_list = list()
		while remaining > 0:
			datasize = min(randint(self.d/2), remaining)  # d/2 just for making more than two packets...
			remaining -= datasize
			pckt_list.append(Packet(_epsilon=0.1, _size=datasize, _log=self.log))

		return pckt_list

	def update_d(self) -> int:
		return self.d

	def append_to_rb_list(self, element: ResourceBlock):
		self.user_rb_list.append(element)
		self.log.infoinfo(msg=f"Appended ResourceBlock to user's rb_list")

	def update_rb_list(self, swap: List[ResourceBlock]) -> List[ResourceBlock]:
		self.user_rb_list = swap
		self.log.info(msg=f"'Updated ResourceBlock to user's rb_list'")
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
