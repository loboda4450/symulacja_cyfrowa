import BTS
import logging


class Network:
	def __init__(self, _epsilon: float, _k: int, _s: int, _l: int, _step_by_step=False):
		self.log: logging.Logger = logging.getLogger(__name__)
		self.k: int = _k  # ilość Resource Blocks
		self.s: int = _s  # czas co ile przydzielane są bloki zasobów RB
		self.epsilon: float = _epsilon  # prawodpodobienstwo przerwania transmisji
		self.clock = 1
		self.bts: BTS = BTS.BTS(k_=self.k, s_=self.s, epsilon_=self.epsilon, clock_=self.clock, _log=self.log)  # stacja bazowa

		self.bts.run(step_by_step=_step_by_step)
