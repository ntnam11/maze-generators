# This algorithm is a randomized version of Kruskal's algorithm.

# 1. Create a list of all walls, and create a set for each cell,
#     each containing just that one cell.
# 2. For each wall, in some random order:
#     1. If the cells divided by this wall belong to distinct sets:
#         1. Remove the current wall.
#         2. Join the sets of the formerly divided cells.

# There are several data structures that can be used to model the sets
# of cells. An efficient implementation using a disjoint-set data structure
# can perform each union and find operation on two sets in nearly
# constant amortized time (specifically, O(alpha V)) time; alpha(x)<5
# for any plausible value of x, so the running time of this algorithm is
# essentially proportional to the number of walls available to the maze.

# It matters little whether the list of walls is initially randomized or
# if a wall is randomly chosen from a nonrandom list, either way is just as easy to code.

# Because the effect of this algorithm is to produce a minimal spanning tree
# from a graph with equally weighted edges, it tends to produce regular patterns
# which are fairly easy to solve.

from common import * 
import random

width = 10
height = 10

# trying to understand the algorithm
# smh