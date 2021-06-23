from datetime import datetime
from statistics import mean
import numpy.random as random

import BTS
import logging
def generate_fucking_random_bigger_than_fucking_0_ffs(l: float) -> int:
    tmp = round(random.exponential(l))
    while tmp <= 3:
        tmp = round(random.exponential(l))

    return tmp

class Network:
    def __init__(self, _epsilon: float, _k: int, _s: int, _t1l: int, _t2l: int,  _step_by_step=False, _simulation_time=60):
        self.log: logging.Logger = logging.getLogger(__name__)
        self.k: int = _k  # ilość Resource Blocks
        self.s: int = _s  # czas co ile przydzielane są bloki zasobów RB
        self.epsilon: float = _epsilon  # prawodpodobienstwo przerwania transmisji
        self.lambdas: tuple = (_t1l, _t2l)
        self.clock = 1
        self.exec_start: datetime = datetime.now()
        self.simulation_time = _simulation_time
        assert _simulation_time >= self.clock
        self.bts: BTS = BTS.BTS(k_=self.k, s_=self.s, epsilon_=self.epsilon, clock_=self.clock,
                                simulation_time_=self.simulation_time, _log=self.log, t1l=generate_fucking_random_bigger_than_fucking_0_ffs(_t1l), t2l=generate_fucking_random_bigger_than_fucking_0_ffs(_t2l))  # stacja bazowa

        self.bts.run(step_by_step=_step_by_step)

    def get_stats(self) -> dict:
        stop = datetime.now()
        return {'simulation start': self.exec_start.strftime("%b %d %Y %H:%M:%S"),
                'simulation end': stop.strftime("%b %d %Y %H:%M:%S"),
                'simulation time': str(stop - self.exec_start),
                'simulated time of': self.simulation_time,
                'users': self.bts.new_users,
                'users served': self.bts.served_users,
                'users to users served ratio': round(self.bts.served_users / self.bts.new_users, 4),
                'cycles done': self.bts.cycles_done,
                'lambdas': self.lambdas,
                'user appearance times': (self.bts.t1, self.bts.t2),
                'user resource blocks propagation properties update': self.bts.tau,
                'mean user wait time': round(mean(self.bts.avg_waittime), 3) if self.bts.avg_waittime else f'ERROR\n {self.bts.avg_waittime}',
                'mean throughput per cycle': round(mean(self.bts.data_sent), 3) if self.bts.data_sent else f'ERROR\n {self.bts.data_sent}',
                'mean retransmitted data per cycle': round(mean(self.bts.data_retransmitted), 3) if self.bts.data_retransmitted else f'ERROR\n {self.bts.data_retransmitted}',
                'mean throughput per user': round(mean(self.bts.user_mean_data_sent), 3) if self.bts.user_mean_data_sent else f'ERROR\n {self.bts.user_mean_data_sent}',
                'mean retransmitted data per user': round(mean(self.bts.user_mean_data_retransmitted), 3) if self.bts.user_mean_data_retransmitted else f'ERROR\n {self.bts.user_mean_data_retransmitted}',
                'user data sent': self.bts.user_mean_data_sent,
                'user data retransmitted': self.bts.user_mean_data_retransmitted,
                'transmission error rate': round(self.bts.error_trasmission / (self.bts.error_trasmission + self.bts.correct_transmission), 4),
                'initial phase cycles': self.bts.initial_phase_cycles}
