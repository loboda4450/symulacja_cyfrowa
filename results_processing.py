from json import load
import matplotlib.pyplot as plt


def main():
    with open('results/2k records.json', 'r') as f:
        results = load(f)

    plt.xlabel('time [s]')
    plt.title('Symulacja Cyfrowa')
    time = [res['simulated time of'] for res in results]
    """USER COUNT IN FIELD OF SIMULATION TIME"""
    # users = [res['users'] for res in results]
    # plt.plot(time, users, label='users in system') # done
    # plt.ylabel('users count')
    """MEAN RETRANSMISSIONS IN FIELD OF SIMULATION TIME"""
    # mn_ret = [res['mean retransmitted data per user'] for res in results]
    # mn_ret_c = [res['mean retransmitted data per cycle'] for res in results]
    # plt.plot(time, mn_ret, label='mean retransmitted data per user') # done
    # plt.plot(time, mn_ret_c, label='mean retransmitted data per cycle') # done
    # plt.ylabel('kBps')
    """MEAN THROUGHPUTS IN FIELD OF SIMULATION TIME"""
    # mn_thr = [res['mean throughput per user'] for res in results]
    # mn_thr_c = [res['mean throughput per cycle'] for res in results]
    # plt.plot(time, mn_thr_c, label='mean throughput per cycle') # done
    # plt.plot(time, mn_thr, label='mean throughput per user') # done
    # plt.ylabel('kBps')
    """MEAN USER WAIT TIME IN FIELD OF SIMULATION TIME"""
    # mn_wtt = [res['mean user wait time'] for res in results]
    # plt.plot(time, mn_wtt, label='mean user wait time') # done
    # plt.ylabel('ms')
    """INITIAL PHASE IN FIELD OF SIMULATION TIME"""
    # in_phase = [res['initial phase cycles'] for res in results]
    # plt.plot(time, in_phase, label='initial phase [cycles]')
    # plt.ylabel('clock cycles')
    """SERVED USERS TO ALL USERS RATIO IN FIELD OF SIMULATION TIME"""
    # served_ratio = [res['users to users served ratio'] for res in results]
    # plt.plot(time, served_ratio, label='served_users : users ratio')
    # plt.ylabel('served users/all users')
    plt.legend()
    plt.show()


if __name__ == '__main__':
    main()
