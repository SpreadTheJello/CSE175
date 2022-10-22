#
# astar.py
#
# This file provides a function implementing A* search for a route finding
# problem. Various search utilities from "route.py" are used in this function,
# including the classes RouteProblem, Node, and Frontier. Also, this function
# uses heuristic function objects defined in the "heuristic.py" file.
#
#
# This code was made by using the A* search psuedocode given in lecture.
# A majority of this code is identical to the code I made in bfs and dfs in PA0.
# A majority of this code is also identical to the greedy.py file. With 
# understanding the route.py and how each object and their methods work, this 
# psuedocode was enough to get started. First I needed to get a starting node 
# Then check if that is the goal state. From their we initialize the frontier. 
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


def a_star_search(problem, h, repeat_check=False):
    """Perform A-Star search to solve the given route finding problem,
    returning a solution node in the search tree, corresponding to the goal
    location, if a solution is found. Only perform repeated state checking if
    the provided boolean argument is true."""

    startNode = Node(problem.start, path_cost= 0.0, h_eval= h.h_cost(problem.start)) # Starting Node with path cost and hcost

    # Immediately check if Node contains goal state and return solution
    if problem.is_goal(startNode.loc):
        return startNode
    
    # Since we're doing uniform cost search, we use a priority queue that sorts by f(n) cost
    nodeFrontier = Frontier(startNode, sort_by ='f')

    # Initializing a set to contain the vistited Nodes and putting the starting one in first.
    if(repeat_check):
        visitedNodes = set()
        visitedNodes.add(startNode)

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
                if node in visitedNodes:
                    # taken from slides: if child is in frontier but with a higher cost
                    if nodeFrontier.contains(node) and (nodeFrontier[node] > node.value("f")):
                        # add child node to the queue and to visited nodes
                        nodeFrontier.add(node)
                        nodeFrontier.add(node)
                else:
                    # add child node to frontier and to visited set
                    nodeFrontier.add(node)
                    visitedNodes.add(node)
            else:   
                # add child node to queue but not in visited
                nodeFrontier.add(node)
    return None
