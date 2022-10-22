#
# heuristic.py
#
# This script defines a utility class that can be used as an implementation
# of a frontier state (location) evaluation function for use in route-finding
# heuristic search algorithms. When a HeuristicSearch object is created,
# initialization code can be executed to prepare for the use of the heuristic
# during search. In particular, a RouteProblem object is typically provided 
# when the HeuristicFunction is created, providing information potentially
# useful for initialization. The actual heuristic cost function, simply
# called "h_cost", takes a state (location) as an argument.
#
#
# This code was made by using information given in lecture.
# Some information was also helped from the CSE175 discord.
# Basically, we can think of speed as the euclidean distance,
# a function given in route.py, divided by the cost of reaching
# that connection. Looping through each connection in the map
# we can caluclate the "speed" given the starting and ending
# (goal) locations. With this we can find the max speed, which
# tells us the speed used in h_cost. the h_cost simply calculates
# the euclidean distance and dividing it by the max speed.
#
# Citations for understanding:
#
# https://blog.finxter.com/python-__delitem__-magic-method/
# https://medium.com/@rinu.gour123/heuristic-search-in-artificial-intelligence-python-3087ecfece4d
# https://www.w3schools.com/python/python_sets.asp
#
# Angelo Fatali - October 25th, 2022
# 
#


import route


class HeuristicFunction:
    """A heuristic function object contains the information needed to
    evaluate a state (location) in terms of its proximity to an optimal
    goal state."""

    def __init__(self, problem=None):
        self.problem = problem

        self.speed = 0.0 # think of speed as distance/cost
        self.distance = 0.0 # distance being our euclidean

        # We need to get map and goal
        self.map = problem.map 
        self.goal = problem.goal # goal is our end location

        # collect all speeds to figure out max speed
        speeds = set()

        # get all the "speeds" for each connection in the map
        for loc in problem.map.loc_dict: # look in our location dictionary
            for connection in problem.map.connection_dict: # look in our connection dictionary
                roadCost = problem.map.get(loc,connection) # get road cost of each connection
                if roadCost != None:
                    euclidean = problem.map.euclidean_distance(loc,connection) # use given euclidean function in route.py
                    speed = euclidean/roadCost
                    speeds.add(speed) # add to total speeds
                
        self.speed = max(speeds) # get highest speed for h_cost

    def h_cost(self, loc=None):
        """An admissible heuristic function, estimating the cost from
        the specified location to the goal state of the problem."""
        # a heuristic value of zero is admissible but not informative
        value = 0.0
        if loc is None:
            return value
        else:
            # PLACE YOUR CODE FOR CALCULATING value OF loc HERE
            euclidean = self.map.euclidean_distance(loc,self.goal)
            value = euclidean/self.speed
            return value

