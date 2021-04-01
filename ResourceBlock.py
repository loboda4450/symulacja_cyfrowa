import logging

import numpy.random as random


class ResourceBlock:
	def __init__(self, _log: bool) -> None:
		self.throughput: int = random.randint(low=20, high=800)  # przepływność użytkownika
		self.log: bool = _log

		if self.log:
			logging.getLogger(__name__).info(msg=f'Created ResourceBlock with throughput of {self.throughput} kbit/s')

	# def __delete__(self, instance):
	# 	del self.throughput
	#
	# 	if self.log:
	# 		logging.getLogger(__name__).info(msg='Removed ResourceBlock')

	def update_throughput(self):
		if self.log:
			logging.getLogger(__name__).info(msg=f"Updating ResourceBlock's throughput to {self.throughput}")

		self.throughput = random.randint(low=20000, high=800000)  # przepływność użytkownika

	def get_throughput(self) -> int:
		if self.log:
			logging.getLogger(__name__).info(msg=f"Getting ResourceBlock's throughput = {self.throughput}")

		return self.throughput
