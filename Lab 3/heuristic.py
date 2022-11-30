#
# heuristic.py
#
# This Python script file provides two functions in support of minimax search
# using the expected value of game states. First, the file provides the
# function "expected_value_over_delays". This function takes as an argument
# a state of game play in which the current player has just selected an
# action. The function calculates the expected value of the state over all
# possible random results determining the amount of time before the
# Guardian changes gaze direction. This function calculates this value
# regardless of whose turn it is. The value of game states that result from
# different random outcomes is determined by calling "value". Second, the
# file provides a heuristic evaluation function for non-terminal game states.
# The heuristic value returned is between "max_payoff" (best for the
# computer player) and negative one times that value (best for the opponent).
# The heuristic function may be applied to any state of play. It uses
# features of the game state to predict the game payoff without performing
# any look-ahead search.
#
# This content is protected and may not be shared, uploaded, or distributed.
#
# PLACE ANY COMMENTS, INCLUDING ACKNOWLEDGMENTS, HERE
#
# Angelo Fatali Nov 29, 2022
#
# My understanding of the game:
# 13 steps each way, meaning (West) -13 -12 .... 12 13 (East), Goal is to get
# to 0 before the computer (west) does, or if the computer gets caught by the
# guardian, the player wins. Computer will start at -13 west, and the player
# at 13 east. The guardian will look in the other direction to whoever is starting
# first, and will have x time until it turns the other direction. This time is
# decided by "flipping a coin", 3 times, and adding the results together. This
# creates a werst and best case scenario, where the worst case is 2, and the best
# case is 5. The player will get to chose their steps, and based off luck, the time
# step will determine uf theyre caught. If the chosen number of steps is greater than
# the time step, then they will get caught. Chosing 1 step is the safest. Minimax
# will be used to look ahead and will try to find the best move. Computer can only
# look ahead 2 moves. The heuristic function will be used to estimate ultity.
#
# Collaborated with Martin Urueta on the heuristic function on a whiteboard (roommate)


from parameters import *
from minimax import probability_of_time
from minimax import value


def expected_value_over_delays(state, ply):
    """Calculate the expected utility over all possible randomly selected
    Guardian delay times. Return this expected utility value."""
    val = 0.0

    # PLACE YOUR CODE HERE
    # Note that the value of "ply" must be passed along, without
    # modification, to any function calls that calculate the value
    # of a state.

    # This was taken from the lecture 11 slides, Uncertainty.
    # EU(A,S) = SUM(Probablity(Result(A,S) | S AND Do(A)) * U(Result(A,S)))
    # Since minimax iterates over all possible states, we need utility and to simply
    # find sum of all probabilities given the delay time. Then multiply probability of
    # time by the value.

    for delay in range(2, 5+1):
        state.time_remaining = delay
        val = val + probability_of_time(delay) * value(state, ply)

    return val


def heuristic_value(state):
    """Return an estimate of the expected payoff for the given state of
    game play without performing any look-ahead search. This value must
    be between the maximum payoff value and the additive inverse of the
    maximum payoff."""
    val = 0.0
    # Going to use -100 -> 100 as payoff due to simplicity.
    # Using location we can easily change the payoff.

    computerVal = abs(board_size) - abs(state.w_loc) # Computer is west
    playerVal = abs(board_size) - abs(state.e_loc) # Player is east

    if (playerVal == computerVal):
        if (state.current_turn is Player.west):
            val = -25
        else:
            val = 25
    elif (playerVal > computerVal): # Will do the inverse of the value
        if (state.current_turn is Player.west):
            val = -100
        else:
            val = -50
    elif (computerVal > playerVal):
        if (state.current_turn is Player.east):
            val = 100
        else:
            val = 50

    return val
