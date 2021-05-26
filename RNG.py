from math import floor, log
from os import urandom


class RNG:
    def __init__(self, init_seed=int.from_bytes(urandom(4), 'little'), _m=2147483647, _a=16807, _q=127773, _r=2836):
        self.seed: int = init_seed
        self.m: int = _m
        self.a: int = _a
        self.q: int = _q
        self.r: int = _r

    def uniform(self) -> float:
        self.seed = int.from_bytes(urandom(4), 'little')  # initialize with new seed value
        h = float(floor(self.seed / self.q))
        self.seed = self.a * (self.seed - (self.q * h)) - self.r * h
        if self.seed < 0:
            self.seed = self.seed + self.m

        return self.seed / self.m

    def exponential(self, l: int) -> float:
        return -(1.0 / l) * log(self.uniform())

    def binary(self, p=0.5) -> bool:
        return self.uniform() > p

    def range(self, start: int, stop: int) -> float:
        return self.uniform() * (stop - start) + start
