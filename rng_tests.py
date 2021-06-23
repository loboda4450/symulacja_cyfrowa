import matplotlib.pyplot as plt
from RNG import RNG
from numpy.random import uniform, exponential, binomial, randint
from os import urandom


def main():
    x = [randint(0, 2147483647) for _ in range(100000)]  # tutaj zmieniamy metodę 'uniform' na inną, aktualnie testowaną, reszta robi się sama. Just python things :D
    plt.hist(x, bins=50)
    plt.show()


if __name__ == '__main__':
    main()
