import logging

import numpy.random as random
from typing import List

import ResourceBlock


class User:
	def __init__(self, resource_blocks: list) -> None:
		self.rb_list: List[ResourceBlock] = resource_blocks  # ilość przydzielonych bloków zasobów
		self.d: int = random.randint(low=1, high=10) * 250  # ilość odbieranych danych przez użytkownika

	def __delete__(self, instance):
		for rb in self.rb_list:
			del rb

		del self.rb_list
		del self.d
		logging.getLogger(__name__).info(msg='Removed BTS user')

	def rb_list_update(self):
		for rb in self.rb_list:
			rb.update_throughput()

		logging.getLogger(__name__).info(msg="Updating user's ResourceBlocks")

	def d_update(self):
		self.d = random.randint(low=1, high=10) * 250
		logging.getLogger(__name__).info(msg="Updating data to receive by user")

	def get_user_throughput(self) -> int:
		logging.getLogger(__name__).info(msg="Getting user's throughput")
		return sum([rb.get_throughput() for rb in self.rb_list])
