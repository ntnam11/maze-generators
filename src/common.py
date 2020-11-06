class Vector2:
    def __init__(self, x, y):
        """Initiate a 2d vector

        Args:
            x (float): x value
            y (float): y value
        """
        self.x = x
        self.y = y

    @staticmethod
    def add(vecA, vecB):
        """Add to vectors

        Args:
            vecA (Vector2): Vector A
            vecB (Vector2): Vector B

        Returns:
            Vector2: Vector result
        """
        return Vector2(vecA.x + vecB.x, vecA.y + vecB.y)

    def __repr__(self):
        return f'({self.x}, {self.y})'

up = Vector2(0, -1)
left = Vector2(-1, 0)
down = Vector2(0, 1)
right = Vector2(1, 0)

directions = [up, left, down, right]

wall_sign = '+'
path_sign = ' '

def movable(pos, visited):
    """Check if the current cell has any unvisited neighbors

    Args:
        pos (Vector2): current cell/position
        visited (list(list(bool))): 2d-list of visited cells

    Returns:
        list(Vector2): neighbor unvisited cells
    """
    result = []
    for direction in directions:
        p = Vector2.add(pos, direction)
        if p.x < 0 or p.x >= len(visited[0]) or \
            p.y < 0 or p.y >= len(visited) or \
            visited[p.y][p.x]:
            continue
        result.append(p)
    return result

def coord_convert(coord_in):
    """Convert the original coordinate to Cell-surrounded coordinate

    Args:
        coord_in (Vector2): Coordinate in m x n matrix

    Returns:
        Vector2: Coordinate in (2m + 1) x (2n + 1) matrix
    """
    return Vector2(coord_in.x * 2 + 1, coord_in.y * 2 + 1)

def draw_paths(width, height, paths):
    """Convert paths to enclosed Cell

    Args:
        width (int): width of the maze
        height (int): height of the maze
        paths (list(tuple(Vector2))): list of tuples of 2 Vector2

    Returns:
        list(list(string)): maze
    """
    width = width * 2 + 1
    height = height * 2 + 1
    result = [[path_sign for x in range(width)] for x in range(height)]

    for y in range(height):
        for x in range(width):
            if x % 2 == 0:
                result[y][x] = wall_sign
            if y % 2 == 0:
                result[y][x] = wall_sign
    
    for p in paths:
        s = Vector2.add(coord_convert(p[0]), coord_convert(p[1]))
        pos_open = Vector2(int(s.x / 2), int(s.y / 2))
        result[pos_open.y][pos_open.x] = ' '

    return result

### Draft section ###

class Cell:
    """Represents a cell (or room) in the maze

    This data structure will be useful in case u wanna draw on screen
    starting from any cell in the maze
    """
    def __init__(self, pos):
        """Initiate a *Cell*

        Args:
            pos (Vector2): position on the map
        """
        self.pos = pos
        self.visited = False
        self.up = None
        self.right = None
        self.down = None
        self.left = None

    def __str__(self):
        s = f'{wall_sign * 3}\n' + f'{wall_sign}{path_sign}{wall_sign}\n' + f'{wall_sign * 3}'

        if self.up is not None:
            s = s[:1] + path_sign + s[2:]
        if self.right is not None:
            s = s[:6] + path_sign + s[7:]
        if self.down is not None:
            s = s[:9] + path_sign + s[10:]
        if self.left is not None:
            s = s[:4] + path_sign + s[5:]
        
        return s

    @staticmethod
    def connect(cell1, cell2):
        """Connect two cells if they can be connected

        Args:
            cell1 (Cell): Cell 1
            cell2 (Cell): Cell 2
        """
        if cell1.pos.x == cell2.pos.x:
            if cell1.pos.y == cell2.pos.y + 1:
                cell1.down = cell2
                cell2.up = cell1
            elif cell1.pos.y == cell2.pos.y - 1:
                cell1.up = cell2
                cell2.down = cell1
        if cell1.pos.y == cell2.pos.y:
            if cell1.pos.x == cell2.pos.x + 1:
                cell1.left = cell2
                cell2.right = cell1
            elif cell1.pos.x == cell2.pos.x - 1:
                cell1.right = cell2
                cell2.left = cell1

    def movable(self, target):
        """Check if able to move from this cell to target

        Args:
            target (Cell): Target Cell
        """
        if target in [self.up, self.right, self.down, self.left]:
            return True
        return False

def draw_Cells(cells):
    """Draw cells

    Args:
        cells (list(list(Cell))): 2d-list of Cells to be drawn
    """
    for row in cells:
        for cell in row:
            print(cell)