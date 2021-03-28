import numpy.random as random


class ResourceBlock:
	def __init__(self) -> None:
		self.throughput: int = random.randint(low=20000, high=800000)  # przepływność użytkownika
