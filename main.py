import logging
import Network
from multiprocessing import Pool, cpu_count
from yaml import dump


def get_work(x):
    network = Network.Network(_epsilon=0.1, _k=15, _s=1, _l=3, _step_by_step=False,
                              _simulation_time=x)  # _step_by_step określa, czy pracujemy krokowo, czy nie
    return network.get_stats()


def main():
    # logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=1)
    # network = Network.Network(_epsilon=0.1, _k=15, _s=1, _l=3, _step_by_step=False,
    #                           _simulation_time=1)  # _step_by_step określa, czy pracujemy krokowo, czy nie
    # print(network.get_stats())

    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]#, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 40, 60, 80, 100, 200, 300, 400, 1000, 2000]
    # arr = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]
    # arr = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3]
    # arr = [1500, 1500, 1500, 1500, 1500, 1500, 1500, 1500, 1500, 1500, 1500, 1500, 1500, 1500, 1500]
    # ~15ms waittime Pan tak powiedział XD

    pool = Pool(cpu_count())
    res = pool.map(get_work, arr)
    pool.close()
    print(dump(res, sort_keys=False, default_flow_style=False))


if __name__ == '__main__':
    main()
