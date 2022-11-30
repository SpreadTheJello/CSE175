#
# main.py
#
# This script provides a top-level driver to play the Guardian Game.
#
# This content is protected and may not be shared, uploaded, or distributed.
#
# David Noelle - Thu Nov  3 16:09:24 PDT 2022
#


import sys
from game import *
from minimax import calculate_time_distribution


def main():
    # initialize the Guardian delay time probability distribution ...
    calculate_time_distribution()
    # the process of game play is in the "play" method ...
    state = Game()
    state.play()
    sys.exit(0)


# In PyCharm, press the green button in the gutter to run the script.
if __name__ == "__main__":
    main()
