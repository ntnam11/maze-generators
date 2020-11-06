# This algorithm is a randomized version of Prim's algorithm.

# 1. Start with a grid full of walls.
# 2. Pick a cell, mark it as part of the maze. Add the walls of the cell to the wall list.
# 3. While there are walls in the list:
#     1. Pick a random wall from the list.
#     If only one of the two cells that the wall divides is visited, then:
#         1. Make the wall a passage and mark the unvisited cell as part of the maze.
#         2. Add the neighboring walls of the cell to the wall list.
#     2. Remove the wall from the list.

# Note that simply running classical Prim's on a graph with random edge weights
# would create mazes stylistically identical to Kruskal's,
# because they are both minimal spanning tree algorithms.
# Instead, this algorithm introduces stylistic variation because the edges closer
# to the starting point have a lower effective weight.

from common import *

width = 10
height = 10

# Start with a grid full of walls

walls = []