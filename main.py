from collections import deque

import pygame as pg
from maze import Maze

# to exit program
from sys import exit

# create window
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 640
WINDOW_CAPTION = "maze-simulation"
WINDOW_COLOR = 'Black'
FRAMERATE = 60

# maze properties
PATH_COLOR = 'Black'
WALL_COLOR = 'Green'
WALL_THICKNESS = 1
MAZE_SCREEN_RATIO = 0.95


def generateDFS(genMaze, start, pathColor):
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


# Create screen
pg.init()
clock = pg.time.Clock()
screen = pg.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pg.display.set_caption(WINDOW_CAPTION)
screen.fill(WINDOW_COLOR)

# create maze background/walls
# TODO: user input dimensions
mazeW = 100
mazeH = 100

# Create un-generated maze:
maze = Maze(mazeW, mazeH, WINDOW_WIDTH, WINDOW_HEIGHT, MAZE_SCREEN_RATIO,
            WALL_THICKNESS, PATH_COLOR, WALL_COLOR)

# Remove later, just for troubleshooting
# for cell in maze.get_cells():
#    print(f"Cell Surface: {cell.cellSurface}, Coords: {cell.coords}")
# for wall in maze.get_walls():
#    print(f"Wall Surface: {wall.wallSurface}, Coords: {wall.coords}")

startCell = maze.get_cells()[0]
# maze.GenerateDFS(startCell, PATH_COLOR)

# Display maze background
screen.blit(maze.BG, maze.coords)
generateDFS(maze, startCell, PATH_COLOR)

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
