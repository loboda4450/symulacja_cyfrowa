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

    def get_stats(self) -> dict:
        stop = datetime.now()
        return {'simulation start': f'{self.exec_start.strftime("%b %d %Y %H:%M:%S")}',
                'simulation end': f'{stop.strftime("%b %d %Y %H:%M:%S")}',
                'simulation time': f'{stop - self.exec_start}',
                'simulated time of': f'{self.simulation_time}s',
                'users': self.bts.new_users,
                'users served': self.bts.served_users,
                'users to users served ratio': f'{round(self.bts.served_users / self.bts.new_users, 4) * 100}%',
                'cycles done': self.bts.cycles_done,
                'user appearance times': f'{self.bts.t1, self.bts.t2}',
                'user resource blocks propagation properties update': self.bts.tau,
                'mean user wait time': f'{round(mean(self.bts.avg_waittime), 3)}ms',
                'transmission error rate': f'{round(self.bts.error_trasmission / (self.bts.error_trasmission + self.bts.correct_transmission), 4) *100}%'}
