import logging
from numpy.random import uniform, randint


class ResourceBlock:
    def __init__(self, _log: logging, _epsilon: float) -> None:
        self.throughput: int = randint(low=20, high=800)  # [bit/ms] przepływność użytkownika
        self.epsilon: float = _epsilon
        self.log: logging.Logger = _log.getChild(__name__)
        self.is_sent: bool = uniform() >= self.epsilon

        self.log.log(msg=f'Created ResourceBlock with throughput of {self.throughput} kbit/s', level=3)

    def update_is_sent(self) -> None:
        self.log.log(msg=f"Updating ResourceBlock's is_sent to {self.is_sent}", level=3)
        self.is_sent = uniform() >= self.epsilon  # random_sample() >= self.epsilon

    def update_throughput(self) -> None:
        self.log.log(msg=f"Updating ResourceBlock's throughput to {self.throughput}", level=3)
        self.throughput = randint(low=20, high=800)  # przepływność użytkownika

    # def get_throughput(self) -> int:
    #     self.log.log(msg=f"Getting ResourceBlock's throughput = {self.throughput}", level=3)
    #     return self.throughput
