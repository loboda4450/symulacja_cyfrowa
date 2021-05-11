from datetime import datetime

import BTS
import logging


class Network:
	def __init__(self, _epsilon: float, _k: int, _s: int, _l: int, _step_by_step=False, _simulation_time=60):
		self.log: logging.Logger = logging.getLogger(__name__)
		self.k: int = _k  # ilość Resource Blocks
		self.s: int = _s  # czas co ile przydzielane są bloki zasobów RB
		self.epsilon: float = _epsilon  # prawodpodobienstwo przerwania transmisji
		self.clock = 1
		self.exec_start: datetime = datetime.now()
		self.bts: BTS = BTS.BTS(k_=self.k, s_=self.s, epsilon_=self.epsilon, clock_=self.clock,
		                        simulation_time_=_simulation_time, _log=self.log)  # stacja bazowa

		self.bts.run(step_by_step=_step_by_step)


	def get_stats(self):
		stop = datetime.now()
		return f'simulation start: {self.exec_start.strftime("%b %d %Y %H:%M:%S")}\n' \
		       f'simulation end: {stop.strftime("%b %d %Y %H:%M:%S")}\n' \
		       f'simulation time: {stop - self.exec_start}\n' \
		       f'users: {self.bts.new_users}\n' \
		       f'users served: {self.bts.served_users}'
