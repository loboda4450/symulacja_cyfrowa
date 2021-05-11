import logging
import Network


def main():
	# logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=1)w
	network = Network.Network(_epsilon=0.1, _k=15, _s=1, _l=3, _step_by_step=False, _simulation_time=1)  # _step_by_step określa, czy pracujemy krokowo, czy nie
	print(network.get_stats())


if __name__ == '__main__':
	main()
