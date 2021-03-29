from time import sleep
import logging

import Network


def main():
	network = Network.Network()
	print('cos musze..')


if __name__ == '__main__':
	logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level='DEBUG')

	main()
	while True:
		sleep(5)
