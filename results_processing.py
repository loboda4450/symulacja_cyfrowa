from json import load
import matplotlib.pyplot as plt
from statistics import mean


def main():
    # l = [[], [], []]
    # for x, y in zip(range(4, 15), range(10, 21)):
    #     with open(f'results/test {x, y}.json', 'r') as f:
    #         results = load(f)
    #     print(f'results for lambdas: {x, y}')
    #     # l[0].append(mean([res['mean throughput per cycle'] for res in results]))
    #     l[2].append(mean([res['initial phase cycles'] for res in results]))
    #     l[1].append(f'{x, y}')
    #
    # plt.figure(figsize=(10, 6))
    # plt.plot(l[1], l[2], label='initial phase cycles')
    # # plt.plot(l[1], l[0], label='mean throughput per cycle')
    # plt.legend()
    # plt.xlabel('lambdas')
    # plt.show()
    #
    # # plt.xlabel('time [s]')
    # # plt.title('Symulacja Cyfrowa')
    # time = [res['simulated time of'] for res in results]
    # """USER COUNT IN FIELD OF SIMULATION TIME"""
    # users = [res['users'] for res in results]
    # # plt.plot(time, users, label='users in system') # done
    # # plt.ylabel('users count')
    # """MEAN RETRANSMISSIONS IN FIELD OF SIMULATION TIME"""
    # mn_ret = [res['mean retransmitted data per user'] for res in results]
    # mn_ret_c = [res['mean retransmitted data per cycle'] for res in results]
    # # plt.plot(time, mn_ret, label='mean retransmitted data per user') # done
    # # plt.plot(time, mn_ret_c, label='mean retransmitted data per cycle') # done
    # # plt.ylabel('kBps')
    # """MEAN THROUGHPUTS IN FIELD OF SIMULATION TIME"""
    # mn_thr = [res['mean throughput per user'] for res in results]
    # mn_thr_c = [res['mean throughput per cycle'] for res in results]
    # # plt.plot(time, mn_thr_c, label='mean throughput per cycle') # done
    # # plt.plot(time, mn_thr, label='mean throughput per user') # done
    # # plt.ylabel('kBps')
    # """MEAN USER WAIT TIME IN FIELD OF SIMULATION TIME"""
    # mn_wtt = [res['mean user wait time'] for res in results]
    # # plt.plot(time, mn_wtt, label='mean user wait time') # done
    # # plt.ylabel('ms')
    # """INITIAL PHASE IN FIELD OF SIMULATION TIME"""
    # in_phase = [res['initial phase cycles'] for res in results]
    # # plt.plot(time, in_phase, label='initial phase [cycles]')
    # # plt.ylabel('clock cycles')
    # """SERVED USERS TO ALL USERS RATIO IN FIELD OF SIMULATION TIME"""
    # # served_ratio = [res['users to users served ratio'] for res in results]
    # # plt.plot(users, mn_thr, label='served_users : users ratio')
    # # plt.ylabel('served users/all users')
    # # plt.legend()
    # # plt.show()
    # # print('mean throughput')
    counter = 0
    with open(f'results/test (9, 15) users spec.json', 'r') as f:
        results = load(f)

    resp = [res['user data sent'] for res in results]

    plt.figure(figsize=(8, 8))
    plt.hist([mean([i1, i2, i3, i4, i5, i6, i7, i8, i9, i10]) for i1, i2, i3, i4, i5, i6, i7, i8, i9, i10 in zip(resp[0], resp[1], resp[2], resp[3], resp[4], resp[5], resp[6], resp[7], resp[8], resp[9])], bins=10)
    plt.ylabel('user count')
    plt.xlabel('user mean throughput')
    plt.savefig(f'plots/mean throughput')






if __name__ == '__main__':
    main()
