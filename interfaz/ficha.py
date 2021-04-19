from .constantes import ROJO, BLANCO, CUADRO, GRIS, CORONA
import pygame

class Ficha:
    PADDING = 15
    OUTLINE = 2

    def __init__(self, row, col, color):
        self.row = row
        self.col = col
        self.color = color
        self.king = False
        self.x = 0
        self.y = 0
        self.calc_pos()

    def calc_pos(self):
        self.x = CUADRO * self.col + CUADRO // 2
        self.y = CUADRO * self.row + CUADRO // 2

    def make_king(self):
        self.king = True
    
    def draw(self, win):
        radius = CUADRO//2 - self.PADDING
        pygame.draw.circle(win, GRIS, (self.x, self.y), radius + self.OUTLINE)
        pygame.draw.circle(win, self.color, (self.x, self.y), radius)
        if self.king:
            win.blit(CORONA, (self.x - CORONA.get_width()//2, self.y - CORONA.get_height()//2))

    def movimiento(self, row, col):
        self.row = row
        self.col = col
        self.calc_pos()

    def __repr__(self):
        return str(self.color)