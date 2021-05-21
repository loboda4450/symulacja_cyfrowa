from math import floor, log
from os import urandom


class RNG:
    def __init__(self, init_seed=int.from_bytes(urandom(2), 'little'), _m=2147483647, _a=16807, _q=127773, _r=2836):
        self.seed: int = init_seed
        self.m: int = _m
        self.a: int = _a
        self.q: int = _q
        self.r: int = _r

    def uniform(self):
        h = floor(self.seed / self.q)
        val = self.a * (self.seed - self.q * h) - self.r * h
        if val < 0:
            val = val + self.m

        return val

    def exponential(self, l: int):
        return -(1.0 / l) * log(self.uniform())

    def binary(self, p=0.5):
        return 1 if self.uniform() > p else 0

    def range(self, start: int, stop: int):
        return self.uniform() * (start - stop) + start
