from collections import deque
import random
from mazegraph import MazeGraph
import pygame as pg


# TODO: create helper functions and decompose
# _initialize_background_, _initialize_cells_and_walls_
class Maze:
    def __init__(self, width, height, windowW=0, windowH=0, windowRatio=0,
                 stroke=0, pathColor='Black', wallColor='Red'):

        # Find dimensions of entire maze
        mazeWidthRatio = width / windowW
        mazeHeightRatio = height / windowH

        # Make sure it always fits on screen
        if mazeWidthRatio >= mazeHeightRatio:
            mazePixelWidth = windowRatio // (1 / windowW)
            heightRatio = width / height
            mazePixelHeight = mazePixelWidth // heightRatio
        else:
            mazePixelHeight = windowRatio // (1 / windowH)
            widthRatio = height / width
            mazePixelWidth = mazePixelHeight // widthRatio

        # Locate coords for maze so it's centered
        self.coords = (windowW - mazePixelWidth) // 2, (windowH - mazePixelHeight) // 2

        # Create MazeGraph of all the cells and walls of the maze
        self.maze = MazeGraph()

        # temporary objects used for the construction of the MazeGraph
        cellNum = 0
        cellSideLen = (mazePixelWidth - (2 * stroke)) // width
        xOffset = (mazePixelWidth - (cellSideLen * width)) // 2
        yOffset = (mazePixelHeight - (cellSideLen * height)) // 2
        startXLocation, cellYLocation = self.coords
        startXLocation += stroke + xOffset
        cellYLocation += stroke + yOffset

        # Create background that fits according to the maze
        mazePixelWidth = cellSideLen * width + 2 * stroke
        mazePixelHeight = cellSideLen * height + 2 * stroke

        self.BG = pg.Surface((mazePixelWidth, mazePixelHeight))
        self.BG.fill(wallColor)

        xCoord = startXLocation - stroke
        yCoord = cellYLocation - stroke

        self.coords = xCoord, yCoord

        cellList = []

        # create graph with given dimensions
        for i in range(height):
            # Each row, the x coordinate resets
            cellXLocation = startXLocation
            for j in range(width):

                currCell = self.maze.add_cell(cellNum, cellSideLen,
                                              (cellXLocation, cellYLocation), pathColor)
                cellList.append(currCell)

                # middle/bottom row cells
                # add edge with above cell
                if i != 0:
                    aboveCellIndex = len(cellList) - width - 1
                    aboveCell = cellList[aboveCellIndex]

                    # Add wall between currCell and aboveCell
                    wallWidth = cellSideLen
                    wallHeight = stroke
                    wallXLocation = cellXLocation
                    wallYLocation = cellYLocation - (stroke / 2)
                    self.maze.add_wall(aboveCell, currCell,
                                       (wallWidth, wallHeight),
                                       (wallXLocation, wallYLocation), 0, wallColor)

                # if not leftmost cell
                # add wall between left cell and currCell
                if j != 0:
                    wallWidth = stroke
                    wallHeight = cellSideLen
                    wallXLocation = cellXLocation - (stroke / 2)
                    wallYLocation = cellYLocation
                    self.maze.add_wall(cellList[-2], currCell,
                                       (wallWidth, wallHeight),
                                       (wallXLocation, wallYLocation), 0, wallColor)

                cellNum += 1

                # Each column, increment x location
                # Each row, increment y location
                cellXLocation += cellSideLen
            cellYLocation += cellSideLen

    # Return all cells in the maze
    def get_cells(self):
        return list(self.maze.walls.keys())

    # Return all walls in the maze
    def get_walls(self):
        walls = set()
        for wallList in self.maze.walls.values():
            walls.update(wallList)
        return list(walls)

    # Generate the maze using a DFS algorithm
    def GenerateDFS(self, startCell, pathColor):

        visitedCells = set()
        stack = deque()

        visitedCells.add(startCell)
        stack.append(startCell)

        while stack:

            currCell = stack.pop()
            nextCell = self.randomUnvisitedNeighbor(currCell, visitedCells)

            if nextCell:

                stack.append(currCell)

                self.breakWall(currCell, nextCell, pathColor)

                visitedCells.add(nextCell)
                stack.append(nextCell)

        return True

    # Returns random unvisited neighbor to the cell
    # if none, returns None
    def randomUnvisitedNeighbor(self, cell, visitedCells):

        unvisitedNeighbors = []

        for neighbor in self.getNeighbors(cell):
            if neighbor not in visitedCells:
                unvisitedNeighbors.append(neighbor)

        if unvisitedNeighbors:
            return random.choice(unvisitedNeighbors)

        return None

    # Returns list of neighboring cells to cell
    def getNeighbors(self, cell):

        neighbors = []

        for wall in self.maze.walls[cell]:
            if wall.cell1 == cell:
                neighbors.append(wall.cell2)
            else:
                neighbors.append(wall.cell1)

        return neighbors

    def breakWall(self, cell1, cell2, pathColor):

        wall = self.maze.get_wall(cell1, cell2)

        if wall:
            wall.weight = 1
            wall.wallSurface.fill(pathColor)
            return True

        return False
