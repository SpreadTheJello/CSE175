#
# dfs.py
#
# This file provides a function implementing depth-first search for a
# route-finding problem. Various search utilities from "route.py" are
# used in this function, including the classes RouteProblem, Node, and
# Frontier.
# 
# Everything is mostly the same from the bfs.py except for some variable names
# to make readability and undestanding more clear. The main difference is the
# Frontier queue boolean to False since DFS uses stacks. 
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


def DFS(problem, repeat_check=False):
    """Perform depth-first search to solve the given route finding
    problem, returning a solution node in the search tree, corresponding
    to the goal location, if a solution is found. Only perform repeated
    state checking if the provided boolean argument is true."""
    
    # PLACE YOUR CODE HERE
    startNode = Node(problem.start) # Starting Node 

    # Immediately check if Node contains goal state and return solution
    if(problem.is_goal(startNode.loc)): #startNode.loc is the location
        return startNode

    # Initialize the frontier according to Stack or Queue
    # DFS means we must use a stack structure: https://www.geeksforgeeks.org/difference-between-bfs-and-dfs/
    nodeStack = Frontier(startNode, False) # This turns the Frontier to implement a stack structure
    
    # Initializing a set to contain the vistited Nodes and putting the starting one in first.
    if(repeat_check):
        visitedNodes = set() # I could have made this a list instead of a set but I wanted to keep consistency
        visitedNodes.add(startNode.loc) 

    # Check if frontier is not empty, then continue
    while(nodeStack.is_empty() == False):
        checked = nodeStack.pop()
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
                    # add child node to the stack and to visited nodes
                    nodeStack.add(eachNode)
                    visitedNodes.add(eachNode.loc)
            else:
                # add chld node to stack but not in visited
                nodeStack.add(eachNode)
    return None
