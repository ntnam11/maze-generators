# A disadvantage of the first approach is a large depth of recursion – in the worst case,
# the routine may need to recur on every cell of the area being processed,
# which may exceed the maximum recursion stack depth in many environments.
# As a solution, the same backtracking method can be implemented with an explicit stack,
# which is usually allowed to grow much bigger with no harm.

# 1. Choose the initial cell, mark it as visited and push it to the stack
# 2. While the stack is not empty
#     1. Pop a cell from the stack and make it a current cell
#     2. If the current cell has any neighbours which have not been visited
#         1. Push the current cell to the stack
#         2. Choose one of the unvisited neighbours
#         3. Remove the wall between the current cell and the chosen cell
#         4. Mark the chosen cell as visited and push it to the stack

from common import * 
import random

width = 10
height = 10

# set start position
start_x = random.randint(0, width)
start_y = random.randint(0, height)

visited = [[False for x in range(width)] for y in range(height)]

pos = Vector2(start_x, start_y)
visited[pos.y][pos.x] = True
paths = []

stack = [pos]

while len(stack) > 0:
    current_pos = stack.pop()
    m = movable(current_pos, visited)
    if len(m) > 0:
        stack.append(current_pos)
        next_pos = random.choice(m)
        stack.append(next_pos)
        
        if not visited[next_pos.y][next_pos.x]:
            visited[next_pos.y][next_pos.x] = True
            paths.append((current_pos, next_pos))
            
result = draw_paths(width, height, paths)
[print('  '.join(x)) for x in result]