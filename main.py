import pygame as pg

# to exit program
from sys import exit

# create window
WINDOW_WIDTH = 400
WINDOW_HEIGHT = 400
MAZE_SCREEN_RATIO = 0.95
WINDOW_CAPTION = "maze-simulation"


# convert cell dimensions to pixel dimensions
def getMazeDimensions(width, height):

    mazePixelWidth, mazePixelHeight = 0, 0

    if width >= height:
        mazePixelWidth = MAZE_SCREEN_RATIO // (1 / WINDOW_WIDTH)
        heightRatio = width / height
        mazePixelHeight = mazePixelWidth // heightRatio
    else:
        mazePixelHeight = MAZE_SCREEN_RATIO // (1 / WINDOW_HEIGHT)
        widthRatio = height / width
        mazePixelWidth = mazePixelHeight // widthRatio

    return mazePixelWidth, mazePixelHeight


# Find coordinates to place maze in center of screen
def getMazeCoords(mazeWidthHeight):
    mazeX, mazeY = mazeWidthHeight
    mazeCoords = ((WINDOW_WIDTH - mazeX) // 2, (WINDOW_HEIGHT - mazeY) // 2)
    return mazeCoords


pg.init()
clock = pg.time.Clock()
screen = pg.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

# create maze background/walls
# TODO: user input dimensions
mazeW = 2
mazeH = 5

mazeDimensions = getMazeDimensions(mazeW, mazeH)
mazeWalls = pg.Surface(mazeDimensions)

# place maze in center
placeMaze = getMazeCoords(mazeDimensions)
mazeWalls.fill('Red')


while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            exit()

    screen.blit(mazeWalls, placeMaze)

    # draw all our elements
    # update everything
    pg.display.update()
    clock.tick(60)

# given the dimension of maze cells, return pixel dimensions
