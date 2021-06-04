import logging
import Network
from multiprocessing import Pool, cpu_count
from json import dumps, dump


def get_work(x):
    network = Network.Network(_epsilon=0.1, _k=15, _s=1, _l=3, _step_by_step=False,
                              _simulation_time=x[0], _t1l=x[1],
                              _t2l=x[2])  # _step_by_step określa, czy pracujemy krokowo, czy nie
    return network.get_stats()


def main():
    # logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=1)

    arr = [[i, 5, 10] for i in range(10, 2000, 10)]
    pool = Pool(cpu_count())
    res = pool.map(get_work, arr)
    pool.close()
    print(dumps(res))
    with open(f'results/tst.json', 'w+') as f:
        dump(res, f, indent=4, separators=(", ", ": "))


if __name__ == '__main__':
    main()
