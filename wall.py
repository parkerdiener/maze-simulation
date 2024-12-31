# Wall class used for connecting Cells
import pygame as pg


class Wall:
    def __init__(self, fromCell, toCell, dimensions, coords, weight=0, color='Black'):
        self.fromCell = fromCell
        self.toVert = toCell
        self.weight = weight
        self.wallSurface = pg.Surface(dimensions)
        self.wallSurface.fill(color)
        self.coords = coords
