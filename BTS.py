import logging
from math import copysign, inf

import numpy.random as random
from typing import List
from ResourceBlock import ResourceBlock
from User import User


def divide(a, b):
    if b == 0:
        return copysign(inf, b)
    else:
        return a / b


def generate_fucking_random_bigger_than_fucking_0_ffs(l: int) -> int:
    tmp = round(random.exponential(l))
    while tmp == 0:
        tmp = round(random.exponential(l))

    return tmp


class BTS:
    def __init__(self, k_: int, s_: int, epsilon_: float, clock_: int, simulation_time_: int, _log: logging):
        self.log: logging.Logger = _log.getChild(__name__)
        self.k: int = k_  # ilość Resource Blocks
        self.k_max: int = 3  # ilość ResourceBlocków do przydzielenie maksymalnie
        self.s: int = s_  # czas co ile przydzielane są bloki zasobów RB
        self.epsilon: float = epsilon_  # prawdopodobienstwo, że transmisja się nie uda
        self.tau: float = generate_fucking_random_bigger_than_fucking_0_ffs(
            10)  # odstęp czasowy między zmianą warunków propagacji dla każdego usera
        self.t1: int = 5  # generate_fucking_random_bigger_than_fucking_0_ffs(40)  # czas co ile pojawiają się nowi userzy
        self.t2: int = 32  # generate_fucking_random_bigger_than_fucking_0_ffs(40)  # czas co ile pojawiają się nowi userzy
        self.clock: int = clock_  # zegar BTSa (1 cykl = 1ms)
        self.cycles_done: int = 0  # wykonane cykle zegarowe przez BTS.
        self.taken_rb_count: int = 0  # ilość zajętych ResourceBlocków
        self.user_list: List[User] = list()  # [User(_log=self.log, _rb=list()) for _ in range(15)]
        self.served_users: int = 0
        self.new_users: int = 0
        self.simulation_time: int = simulation_time_ * 1000
        self.avg_waittime: List[int] = list()
        self.correct_transmission = 0
        self.error_trasmission = 0
        self.initial_phase: bool = False
        self.initial_phase_cycles: int = None

        self.log.log(msg='Created Base Transmitting Station', level=1)

    def run(self, step_by_step: bool):
        while self.simulation_time >= self.cycles_done:
            self.step()

            if step_by_step:
                if input('Press "Enter" to continue, ":q!" then "Enter" to exit simulation...\n') == ':q!':
                    exit(0)

    def step(self):
        if not self.cycles_done % self.t1:
            self.add_user()
            self.log.log(msg='Added user with t1', level=1)

        if not self.cycles_done % self.t2:
            self.add_user()
            self.log.log(msg='Added user with t2', level=1)

        if not self.cycles_done % self.tau:
            self.update_users_throughput()
            self.log.log(msg='Updated users propagation conditions', level=1)

        if not self.cycles_done % self.s and self.user_list:
            self.redistribute_resource_blocks()
            self.log.log(msg='Updated users resource blocks', level=1)

        for user in self.user_list:
            if user.d > 0 and user.has_resource_blocks():
                for rb in user.user_rb_list:
                    if rb.is_sent:
                        user.d -= rb.throughput
                        self.correct_transmission += 1
                        self.log.log(msg='Sent packet!', level=1)
                    else:
                        rb.update_is_sent()
                        self.error_trasmission += 1
                        self.log.log(msg='Packet updated!', level=2)

                user.update_prev_sum_d()

                if user.d <= 0:
                    if self.initial_phase: self.avg_waittime.append(user.waittime)
                    self.remove_user(user)

            user.update_user_waittime()

        self.cycles_done += self.clock

    def add_user(self) -> None:
        self.user_list.append(User(_log=self.log, _rb=list()))
        self.new_users += 1

        self.log.log(msg='Added user to BTS!', level=1)

    def remove_user(self, user: User) -> None:
        self.taken_rb_count -= len(user.user_rb_list)
        self.user_list.remove(user)
        self.served_users += 1

        self.log.log(msg='Removed user!', level=1)

    def update_users_throughput(self) -> None:  # Update throughput of existing ResourceBlocks
        for user in self.user_list:
            user.update_user_existing_rbs()

    def redistribute_resource_blocks(self) -> None:
        for user in self.user_list:
            user.clear_resource_blocks()

        for i in range(len(self.user_list) * self.k_max if len(self.user_list) < self.k / self.k_max else self.k):
            value, user_index = max(
                ((divide(user.get_current_throughput(), user.get_avg_throughput()), user_index) for user_index, user in
                 enumerate(self.user_list) if not user.has_all_resource_blocks()), key=lambda x: x[0])
            picked = self.user_list[user_index]

            picked.add_resource_block(ResourceBlock(_log=self.log, _epsilon=self.epsilon))

            if i == self.k - 1 and not self.initial_phase:
                self.initial_phase = True
                self.initial_phase_cycles = self.cycles_done
