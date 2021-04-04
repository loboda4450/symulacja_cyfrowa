from time import sleep
import logging

import Network


def main():
	logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level='DEBUG')
	network = Network.Network(_epsilon=0.1, _k=15, _s=1, _l=3, _step_by_step=False)  # _step_by_step określa, czy pracujemy krokowo, czy nie


if __name__ == '__main__':
	main()
