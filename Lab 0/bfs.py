#
# bfs.py
#
# This file provides a function implementing breadth-first search for a
# route-finding problem. Various search utilities from "route.py" are
# used in this function, including the classes RouteProblem, Node, and
# Frontier.
#
# This code was made by using the generic seaarch psuedocode given in lecture.
# With understanding the route.py and how each object and their methods work,   
# this psuedocode was enough to get started. First I needed to get a starting
# node and its location. Then check if that is the goal state. From their we
# initialize the frontier according to queue or stack. While the frontier is
# not empty we simply remove it from frontier. if the node is the goal state 
# we return it. EXpand the node to see it's chidlren, check each children if
# repeated check is on and if its already visited, add accordingly to the
# frontier.
#
# Citations for understanding:
#
# https://www.geeksforgeeks.org/difference-between-bfs-and-dfs/
# https://www.w3schools.com/python/python_sets.asp
# https://www.educative.io/answers/how-to-implement-a-breadth-first-search-in-python
# Worked with Martin Urueta on a whiteboard to understand BFS and DFS together (roommate)
#
# Angelo Fatali - October 4th, 2022
# 


from route import Node
from route import Frontier


def BFS(problem, repeat_check=False):
    """Perform breadth-first search to solve the given route finding
    problem, returning a solution node in the search tree, corresponding
    to the goal location, if a solution is found. Only perform repeated
    state checking if the provided boolean argument is true."""

    # PLACE YOUR CODE HERE
    startNode = Node(problem.start) # Starting Node 

    # Immediately check if Node contains goal state and return solution
    if(problem.is_goal(startNode.loc)): #startNode.loc is the location
        return startNode

    # Initialize the frontier according to Stack or Queue
    # BFS means we must use a queue structure: https://www.geeksforgeeks.org/difference-between-bfs-and-dfs/
    nodeQueue = Frontier(startNode, True) # This turns the Frontier to implement a queue structure
    
    # Initializing a set to contain the vistited Nodes and putting the starting one in first.
    if(repeat_check): # originally I wasn't checking for repeated check and got an extra node expansion, this is needed to lower the expansion
        visitedNodes = set() # I could have made this a list instead of a set but I wanted to keep consistency
        visitedNodes.add(startNode.loc)

    # Check if frontier is not empty, then continue
    while(nodeQueue.is_empty() == False):
        checked = nodeQueue.pop()
        # check if we found our solution based off of the checked node location
        if (problem.is_goal(checked.loc)):
            return checked
        # expands the checked nodes and gets a list of all reachable nodes (checked node's children)
        reachableNodes = checked.expand(problem)

        # check all reachableNodes from the checked ones
        for eachNode in reachableNodes:
            # continue only if we need to, and if the child node is not already visited
            if(repeat_check == True):
                if(eachNode.loc not in visitedNodes):
                    # add child node to the queue and to visited nodes
                    nodeQueue.add(eachNode)
                    visitedNodes.add(eachNode.loc)
            else:
                # add chld node to queue but not in visited
                nodeQueue.add(eachNode)

    return None
