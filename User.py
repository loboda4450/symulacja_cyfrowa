import logging
from typing import List
from ResourceBlock import ResourceBlock

# from numpy.random import randint


class User:
	def __init__(self, _log: logging, _rb: List[ResourceBlock]):
		self.log: logging.Logger = _log.getChild(__name__)
		self.user_id: int = 0
		self.d: int = 2000 # randint(low=1, high=10) * 250  # [b] losowa (rozkład jednostajny) liczba odbieranych danych przez użytkownika
		self.user_rb_list: List[ResourceBlock] = _rb  # lista przydzielonych bloków zasobów użytkownikowi
		self.prev_sum_d: List[int] = list()  # lista przepływności z poprzednich 5 ms.
		self.sum_d: List[ResourceBlock] = list()  # nie ma sensu z tego wyciągać średniej, jeżeli numa >= numb, to numa/5 >= numb/5

	# self.log.log(msg=f'Created user: {self.d, self.user_rb_list, self.sum_d}', level=2)

	# def update_avg_throughput(self):
	# 	self.prev_sum_d.append(sum([rb.throughput for rb in self.user_rb_list]))
	# 	if len(self.user_rb_list) > 5:
	# 		self.user_rb_list.remove(self.user_rb_list[0])

	def send_packet(self) -> None:
		for rb in self.user_rb_list:
			if rb.is_sent:
				self.d -= rb.throughput
				self.log.log(msg='Sent packet!', level=2)
			else:
				rb.update_is_sent()
				self.log.log(msg='Packet updated!', level=2)

	# def update_d(self) -> None:
	# 	self.d = randint(low=1, high=10) * 250

	def has_resource_blocks(self) -> bool:
		return len(self.user_rb_list) > 0

	def add_resource_block(self, _rb: ResourceBlock) -> None:
		self.user_rb_list.append(_rb)
		self.sum_d = self.user_rb_list

	def has_all_resource_blocks(self) -> bool:
		return len(self.user_rb_list) == 3

	def clear_resource_blocks(self) -> None:
		self.prev_sum_d = [sum(rb.throughput for rb in self.user_rb_list)]
		self.user_rb_list = list()

	# self.log.log(msg=f"Appended ResourceBlock to user's rb_list", level=2)

	def update_user_existing_rbs(self) -> None:
		for rb in self.user_rb_list:
			rb.update_throughput()

	# self.log.log(msg=f"Updated ResourceBlock to user's rb_list", level=2)

	def update_prev_sum_d(self) -> None:
		self.prev_sum_d.append(sum(rb.throughput for rb in self.user_rb_list))
		if len(self.prev_sum_d) > 5:
			self.prev_sum_d.pop(0)

	def update_sum_d(self) -> None:
		self.sum_d = sum(rb.throughput for rb in self.user_rb_list if rb.is_sent)

	def get_avg_throughput(self) -> int:
		return sum(self.prev_sum_d)

	def get_current_throughput(self) -> int:
		return sum(rb.throughput for rb in self.sum_d)
