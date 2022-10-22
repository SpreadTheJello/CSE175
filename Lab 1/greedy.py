#
# greedy.py
#
# This file provides a function implementing greedy best-first search for
# a route finding problem. Various search utilities from "route.py" are
# used in this function, including the classes RouteProblem, Node, and
# Frontier. Also, this function uses heuristic function objects defined
# in the "heuristic.py" file.
#
#
# This code was made by using the greedy search psuedocode given in lecture.
# A majority of this code is identical to the code I made in bfs and dfs in PA0.
# With understanding the route.py and how each object and their methods work,   
# this psuedocode was enough to get started. First I needed to get a starting
# node and its location, and pass it h_eval to be our heuristic function. Then 
# check if that is the goal state. From their we initialize the frontier. 
# While the frontier is not empty we simply remove it from frontier. If the 
# node is the goal state we return it. Expand the node to see it's children, 
# check each children if repeated check is on and if its already visited, 
# add accordingly to the frontier.
#
# Citations for understanding:
#
# https://blog.finxter.com/python-__delitem__-magic-method/
# https://medium.com/@rinu.gour123/heuristic-search-in-artificial-intelligence-python-3087ecfece4d
# https://www.w3schools.com/python/python_sets.asp
#
# Angelo Fatali - October 25th, 2022
# 


from route import Node
from route import Frontier


def greedy_search(problem, h, repeat_check=False):
    """Perform greedy best-first search to solve the given route finding
    problem, returning a solution node in the search tree, corresponding
    to the goal location, if a solution is found. Only perform repeated
    state checking if the provided boolean argument is true."""

    startNode = Node(problem.start, h_eval = h.h_cost(problem.start)) # Starting Node

    # Immediately check if Node contains goal state and return solution
    if problem.is_goal(startNode.loc): #startNode.loc is the location
        return startNode
    
    # Since we're doing greedy search, we use a priority queue that sorts by h(n) cost
    nodeFrontier = Frontier(startNode, sort_by = 'h') 
    
    # Initializing a set to contain the vistited Nodes and putting the starting one in first.
    if(repeat_check):
        visitedNodes = set()
        visitedNodes.add(startNode.loc)

    # Check if frontier is not empty, then continue
    while (nodeFrontier.is_empty() == False):
        checked = nodeFrontier.pop()
        # check if we found our solution based off of the checked node location
        if problem.is_goal(checked.loc):
            return checked
        # expands the checked nodes and gets a list of all reachable nodes (checked node's children)    
        reachableNodes = checked.expand(problem, h_fun = h)

        # check all reachableNodes from the checked ones
        for node in reachableNodes:
            # continue only if we need to, and if the child node is not already visited
            if repeat_check == True:
                if node not in visitedNodes:
                    # add child node to the queue and to visited nodes
                    visitedNodes.add(node)
                    nodeFrontier.add(node)
            else:
                # add child node to queue but not in visited
                nodeFrontier.add(node)

    return None
