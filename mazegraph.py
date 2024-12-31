from cell import Cell
from wall import Wall

# Graph class
# TODO add more header comment


class MazeGraph:
    def __init__(self):
        self.walls = {}

    def add_cell(self, label, side_len, coords, color='Black'):
        # Create and add a new cell
        cell = Cell(label, side_len, coords, color)
        if cell not in self.walls:
            self.walls[cell] = []
        return cell

    def add_wall(self, cell1, cell2, dimensions, coords, weight=0, color='Black'):
        # Create and add a new wall
        wall = Wall(cell1, cell2, dimensions, coords, weight, color)
        self.walls[cell1].append(wall)
        self.walls[cell2].append(wall)

    def has_wall(self, cell1, cell2):
        # Check if a wall exists between two cells
        for wall in self.walls.get(cell1, []):
            if wall.toCell == cell2 and wall.weight == 0:
                return True
        return False
