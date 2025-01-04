# Wall class used for connecting Cells
import pygame as pg


class Wall:
    def __init__(self, cell1, cell2, dimensions, coords, weight=0, color='Black'):
        self.cell1 = cell1
        self.cell2 = cell2
        self.weight = weight
        self.wallSurface = pg.Surface(dimensions)
        self.wallSurface.fill(color)
        self.coords = coords

    def __repr__(self):
        return f"{self.cell1} - {self.cell2}"
