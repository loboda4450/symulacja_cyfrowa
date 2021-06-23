import logging
import Network
from multiprocessing import Pool, cpu_count
from json import dumps, dump


def get_work(x):
    network = Network.Network(_epsilon=0.1, _k=15, _s=1, _step_by_step=False,
                              _simulation_time=x[0], _t1l=x[1],
                              _t2l=x[2])
    z = network.get_stats()
    return z


def main():
    # regular run
    # logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=1)
    # network = Network.Network(_epsilon=0.1, _k=15, _s=1, _step_by_step=False,
    #                           _simulation_time=10, _t1l=5,
    #                           _t2l=10)
    # print(network.get_stats())

    # multithread run
    pool = Pool(cpu_count())
    # for a, b in zip(range(4, 15, 1), range(10, 21, 1)):
    arr = [[10, 9, 15]] * 10
    res = pool.map(get_work, arr)

    print(dumps(res))
    with open(f'results/test {9, 15} users spec.json', 'w+') as f:
        dump(res, f, indent=4, separators=(", ", ": "))

    pool.close()


if __name__ == '__main__':
    main()
