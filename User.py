import logging
from typing import List
from ResourceBlock import ResourceBlock
from Packet import Packet

from numpy.random import randint


class User:
	def __init__(self, _log: logging):
		self.log: logging.Logger = _log.getChild(__name__)
		self.user_id: int = 0
		self.d: int = randint(low=1, high=10) * 250  # [b] losowa (rozkład jednostajny) liczba odbieranych danych przez użytkownika
		self.user_rb_list: List[ResourceBlock] = [ResourceBlock(_log=self.log) for _ in range(3)]  # lista przydzielonych bloków zasobów użytkownikowi
		# self.packet_list: List[Packet] = self.generate_packets()  # lista pakietów przypisanych do użytkownika
		self.prev_sum_d: int = 0  # średnia przepływność z poprzednich 5 ms.
		self.sum_d: int = 0  # nie ma sensu z tego wyciągać średniej, jeżeli numa >= numb, to numa/5 >= numb/5

		# self.log.log(msg=f'Created user: {self.d, self.user_rb_list, self.sum_d}', level=2)

	# def generate_packets(self):
	# 	remaining = self.d
	# 	pckt_list = list()
	# 	while remaining > 0:
	# 		datasize = min(randint(self.d/2), remaining)  # d/2 just for making more than two packets...
	# 		remaining -= datasize
	# 		pckt_list.append(Packet(_epsilon=0.1, _size=datasize, _log=self.log))
	#
	# 	return pckt_list

	def send_packet(self) -> None:
		for rb in self.user_rb_list:
			if rb.is_sent:
				self.d -= rb.throughput

	def update_d(self) -> int:
		return self.d

	def append_to_rb_list(self, element: ResourceBlock) -> None:
		self.user_rb_list.append(element)
		self.log.log(msg=f"Appended ResourceBlock to user's rb_list", level=2)

	def update_rb_list(self, swap: List[ResourceBlock]) -> List[ResourceBlock]:
		self.user_rb_list = swap
		self.update_prev_sum_d(old_sum=self.sum_d)
		self.update_sum_d()
		self.log.log(msg=f"'Updated ResourceBlock to user's rb_list'", level=2)
		return self.user_rb_list

	def update_prev_sum_d(self, old_sum: int) -> None:
		self.prev_sum_d = old_sum

	def update_sum_d(self) -> None:
		self.sum_d = sum(rb.throughput for rb in self.user_rb_list)
