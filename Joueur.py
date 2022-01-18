import pygame
from pygame.math import Vector2

import core


class Joueur:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.position = Vector2(self.x, self.y)
        self.direction = Vector2(0, 0)

    def draw(self, screen):
        pygame.draw.rect(core.screen, (255, 255, 255), pygame.Rect(self.x, self.y, 10, 100))

    def deplacer(self, direction):
        if direction == 1:
            if self.y > 0:
                self.y = self.y - 2
            else:
                self.y = self.y
        if direction == 2:
            if self.y < 620:
                self.y = self.y + 2
            else:
                self.y = self.y
