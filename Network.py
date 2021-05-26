from datetime import datetime
from statistics import mean

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
        self.simulation_time = _simulation_time
        assert _simulation_time >= self.clock
        self.bts: BTS = BTS.BTS(k_=self.k, s_=self.s, epsilon_=self.epsilon, clock_=self.clock,
                                simulation_time_=self.simulation_time, _log=self.log)  # stacja bazowa

        self.bts.run(step_by_step=_step_by_step)

    def get_stats(self):
        stop = datetime.now()
        return f'simulation start: {self.exec_start.strftime("%b %d %Y %H:%M:%S")}\n' \
               f'simulation end: {stop.strftime("%b %d %Y %H:%M:%S")}\n' \
               f'simulation time: {stop - self.exec_start}\n' \
               f'simulated time of: {self.simulation_time}s\n' \
               f'users: {self.bts.new_users}\n' \
               f'users served: {self.bts.served_users}\n' \
               f'users to users served ratio: {round(self.bts.served_users/(self.bts.new_users), 4)*100}%\n' \
               f'cycles done: {self.bts.cycles_done}\n' \
               f'user appearance times: {self.bts.t1, self.bts.t2}\n' \
               f'user resource blocks propagation properties update: {self.bts.tau}\n' \
               f'mean user wait time: {round(mean(self.bts.avg_waittime), 3)}ms\n' \
               f'transmission error rate: {round(self.bts.error_trasmission/(self.bts.error_trasmission + self.bts.correct_transmission), 4)*100}%'
