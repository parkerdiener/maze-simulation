import random
import time
from collections import deque
import pygame as pg
from maze import Maze
from cellSetCollection import cellSetCollection

# to exit program
from sys import exit

# create window
WINDOW_WIDTH = 1280
WINDOW_HEIGHT = 720
WINDOW_CAPTION = "maze-simulation"
WINDOW_COLOR = 'Black'
FRAMERATE = 60

# maze properties
PATH_COLOR = 'Black'
WALL_COLOR = 'Green'
WALL_THICKNESS = 2
MAZE_SCREEN_RATIO = 0.95


# generate the maze using DFS
def generateDFS(genMaze, pathColor):
    start = maze.get_cells()[0]
    visitedCells = set()
    stack = deque()

    visitedCells.add(start)
    stack.append(start)

    while stack:

        currCell = stack.pop()
        nextCell = genMaze.randomUnvisitedNeighbor(currCell, visitedCells)

        if nextCell:
            stack.append(currCell)

            genMaze.breakWall(currCell, nextCell, pathColor)

            visitedCells.add(nextCell)
            stack.append(nextCell)

            # Display maze cells and walls
            for cell in maze.get_cells():
                screen.blit(cell.cellSurface, cell.coords)

            for wall in maze.get_walls():
                screen.blit(wall.wallSurface, wall.coords)

            pg.display.update()
            clock.tick(FRAMERATE)

    return True


# generate the maze using Kruskal's algorithm
def generateKruskal(genMaze, pathColor):

    wallList = genMaze.get_walls()

    # Merge different sets until they're all connected
    cellSets = cellSetCollection(genMaze.get_cells())
    while wallList:
        nextWall = random.choice(wallList)
        wallList.remove(nextWall)

        set1 = cellSets.getSet(nextWall.cell1)
        set2 = cellSets.getSet(nextWall.cell2)

        if set1 != set2:
            cellSets.merge(set1, set2)
            genMaze.breakWall(nextWall.cell1, nextWall.cell2, pathColor)

        # Display maze cells and walls
        for cell in maze.get_cells():
            screen.blit(cell.cellSurface, cell.coords)

        for wall in maze.get_walls():
            screen.blit(wall.wallSurface, wall.coords)

        pg.display.update()
        clock.tick(FRAMERATE)

    return True


# Create screen
pg.init()
clock = pg.time.Clock()
screen = pg.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pg.display.set_caption(WINDOW_CAPTION)
screen.fill(WINDOW_COLOR)

# create maze background/walls
# TODO: user input dimensions
mazeW = 30
mazeH = 30

# Create un-generated maze:
maze = Maze(mazeW, mazeH, WINDOW_WIDTH, WINDOW_HEIGHT, MAZE_SCREEN_RATIO,
            WALL_THICKNESS, PATH_COLOR, WALL_COLOR)

# Display maze background
screen.blit(maze.BG, maze.coords)

startTime = time.time()
# Display animated maze generation
generateKruskal(maze, PATH_COLOR)
endTime = time.time()
# See how long it took to generate
print(endTime - startTime)

# Keep displaying finished maze
while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            exit()

    # Display maze background
    screen.blit(maze.BG, maze.coords)

    # Display maze cells and walls
    for cell in maze.get_cells():
        screen.blit(cell.cellSurface, cell.coords)

    for wall in maze.get_walls():
        screen.blit(wall.wallSurface, wall.coords)

    pg.display.update()
    clock.tick(FRAMERATE)
