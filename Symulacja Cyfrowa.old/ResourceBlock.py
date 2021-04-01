import logging

import numpy.random as random


class ResourceBlock:
	def __init__(self) -> None:
		self.throughput: int = random.randint(low=20, high=800) * 1000  # przepływność użytkownika
		logging.getLogger(__name__).info(msg=f'Created ResourceBlock with throughput = {self.throughput}')

	def __delete__(self, instance):
		del self.throughput
		logging.getLogger(__name__).info(msg='Removed ResourceBlock')

	def update_throughput(self):
		self.throughput = random.randint(low=20000, high=800000)  # przepływność użytkownika
		logging.getLogger(__name__).info(msg=f"Updating ResourceBlock's throughput to {self.throughput}")

	def get_throughput(self) -> int:
		logging.getLogger(__name__).info(msg=f"Getting ResourceBlock's throughput = {self.throughput}")
		return self.throughput
