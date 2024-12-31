# Cell class
import pygame as pg


class Cell:
    def __init__(self, label, side_len, coords, color='Black'):
        self.label = label
        self.cellSurface = pg.Surface((side_len, side_len))
        self.cellSurface.fill(color)
        self.coords = coords

