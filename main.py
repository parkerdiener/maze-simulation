import pygame

# to exit program
from sys import exit

WINDOW_WIDTH = 400
WINDOW_HEIGHT = 400
WINDOW_CAPTION = "maze-simulation"

pygame.init()
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    # draw all our elements
    # update everything
    pygame.display.update()
