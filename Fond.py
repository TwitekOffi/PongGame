import pygame

import core


class Fond:
    def __init__(self):
        self.x = 0
        self.y = 0

    def draw(self, screen):
        pygame.draw.rect(core.screen, (255, 255, 255), pygame.Rect(540, 0, 1, 720))

    def updatescore(self, score):
        core.Draw.text((255, 255, 255), str(score), (self.x, self.y), 75, 'Comic Sans MS')
