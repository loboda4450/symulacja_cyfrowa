import logging
import Network
from RNG import RNG
from multiprocessing import Pool, cpu_count


def get_work(x):
    network = Network.Network(_epsilon=0.1, _k=15, _s=1, _l=3, _step_by_step=False,
                              _simulation_time=x)  # _step_by_step określa, czy pracujemy krokowo, czy nie
    return network.get_stats()


def main():
    # logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=1)
    # network = Network.Network(_epsilon=0.1, _k=15, _s=1, _l=3, _step_by_step=False,
    #                           _simulation_time=1)  # _step_by_step określa, czy pracujemy krokowo, czy nie
    # print(network.get_stats())

    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

    pool = Pool(cpu_count())
    res = pool.map(get_work, arr)
    pool.close()
    for r in res:
        print(r + '\n')


if __name__ == '__main__':
    main()
