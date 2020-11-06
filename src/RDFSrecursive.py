# The depth-first search algorithm of maze generation is frequently implemented using backtracking.
# This can be described with a following recursive routine:
#
# 1. Given a current cell as a parameter,
# 2. Mark the current cell as visited
# 3. While the current cell has any unvisited neighbour cells
#   1. Choose one of the unvisited neighbours
#   2. Remove the wall between the current cell and the chosen cell
#   3. Invoke the routine recursively for a chosen cell
#
# which is invoked once for any initial cell in the area.

from common import * 
import random

width = 10
height = 10

# set start position
start_x = random.randint(0, width)
start_y = random.randint(0, height)
pos = Vector2(start_x, start_y)

def RDFSrecursive():
    """RDFS, recursive version
    Using plain *visited* 2d-list and a *paths* to indicate
    possible movement between cells 
    """

    visited = [[False for x in range(width)] for y in range(height)]
    visited[pos.y][pos.x] = True
    paths = []

    def move(current_pos):

        # While the current cell has any unvisited neighbor cells
        m = movable(current_pos, visited)
        while len(m) > 0:
            
            # Chose one randomly
            next_pos = random.choice(m)

            if not visited[next_pos.y][next_pos.x]:

                # Mark the chosen cell as visited and set as movable path
                visited[next_pos.y][next_pos.x] = True
                paths.append((current_pos, next_pos))

                # Invoke the routine recursively
                move(next_pos)
            
            # Remove the chosen cell from neibors
            m.remove(next_pos)

    move(pos)

    # Convert to enclosed cells
    result = draw_paths(width, height, paths)

    # Print the result
    [print('  '.join(x)) for x in result]

RDFSrecursive()

### Draft section ###

def RDFSrecursive_Cells():
    """RDFS, recursive version
    Transform the result to *Cell* data structure
    """
    cells = [[Cell(Vector2(x, y)) for x in range(width)] for y in range(height)]

    def move(current_pos):
        current_cell = Cell(current_pos)
        movable_cells = []

        for d in directions:
            next_pos = Vector2.add(current_cell.pos, d)
            if next_pos.x < 0 or next_pos.x >= width or \
                next_pos.y < 0 or next_pos.y >= height:
                continue
            movable_cells.append(next_pos)
        
        while len(movable_cells) > 0:
            next_pos = random.choice(movable_cells)
            next_cell = cells[next_pos.y][next_pos.x]

            if not next_cell.visited:
                Cell.connect(current_cell, next_cell)
                next_cell.visited = True
                move(next_pos)

            movable_cells.remove(next_pos)

    move(pos)
    draw_Cells(cells)