import sys
from simulation import Simulation


def main(argv):
    simulation = Simulation()
    simulation.process()


if __name__ == "__main__":
    main(sys.argv)
