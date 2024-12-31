import pygame as pg
from maze import Maze

# to exit program
from sys import exit

# create window
WINDOW_WIDTH = 400
WINDOW_HEIGHT = 400
WINDOW_CAPTION = "maze-simulation"
WINDOW_COLOR = 'Pink'

# maze properties
PATH_COLOR = 'Black'
WALL_COLOR = 'Red'
WALL_THICKNESS = 2
MAZE_SCREEN_RATIO = 0.95

# Create screen
pg.init()
clock = pg.time.Clock()
screen = pg.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pg.display.set_caption(WINDOW_CAPTION)
screen.fill(WINDOW_COLOR)

# create maze background/walls
# TODO: user input dimensions
mazeW = 30
mazeH = 20

# Create un-generated maze:
maze = Maze(mazeW, mazeH, WINDOW_WIDTH, WINDOW_HEIGHT, MAZE_SCREEN_RATIO,
            WALL_THICKNESS, PATH_COLOR, WALL_COLOR)

for cell in maze.get_cells():
    print(f"Cell Surface: {cell.cellSurface}, Coords: {cell.coords}")
for wall in maze.get_walls():
    print(f"Wall Surface: {wall.wallSurface}, Coords: {wall.coords}")

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
    clock.tick(60)
