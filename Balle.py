import pygame
from pygame.math import Vector2
import core


class Balle:
    def __init__(self):
        self.couleur = (255, 255, 255)
        self.position = Vector2(540, 360)
        self.rayon = 5
        self.direction = Vector2(0, 0)

        self.Fx = 0
        self.Ux = Vector2(0, 0)
        self.l = 0
        self.l0 = 10
        self.L = 0

    def draw(self, screen):
        pygame.draw.circle(screen, self.couleur, self.position, self.rayon)

    def deplacer(self,h,l, J1, J2):
        # if self.position.x < 0 or self.position.x > l:
        #     self.direction = Vector2(self.direction.x * -1, self.direction.y)
        if self.position.x < (core.memory("Joueur1").x+10) and (self.position.y > core.memory("Joueur1").y and (self.position.y < (core.memory("Joueur1").y+100))) or self.position.x > (core.memory("Joueur2").x) and (self.position.y > core.memory("Joueur2").y and (self.position.y < (core.memory("Joueur2").y+100))):
            self.direction = Vector2(self.direction.x * -1, self.direction.y)
        if self.position.x < 0:
            core.memory("J2", core.memory("J2") + 1)
            core.memory("ScoreJ2").updatescore(J2)
            self.position.x = 540
            self.position.y = 360
            self.direction = Vector2(0, 0)
            core.memory("Joueur1").x = 10
            core.memory("Joueur1").y = 310
            core.memory("Joueur1").position = Vector2(core.memory("Joueur1").x, core.memory("Joueur1").y)
            core.memory("Joueur2").x = 1060
            core.memory("Joueur2").y = 310
            core.memory("Joueur2").position = Vector2(core.memory("Joueur2").x, core.memory("Joueur2").y)
            core.memory("LastWinner", 2)
        if self.position.x > 1080:
            core.memory("J1", core.memory("J1")+1)
            core.memory("ScoreJ1").updatescore(J1)
            self.position.x = 540
            self.position.y = 360
            self.direction = Vector2(0, 0)
            core.memory("Joueur1").x = 10
            core.memory("Joueur1").y = 310
            core.memory("Joueur1").position = Vector2(core.memory("Joueur1").x, core.memory("Joueur1").y)
            core.memory("Joueur2").x = 1060
            core.memory("Joueur2").y = 310
            core.memory("Joueur2").position = Vector2(core.memory("Joueur2").x, core.memory("Joueur2").y)
            core.memory("LastWinner", 1)
        if self.position.y < 0 or self.position.y > h:
            self.direction = Vector2(self.direction.x, self.direction.y * -1)

        self.position = self.direction + self.position

        if core.getKeyPressList("g"):
            if core.memory("LastWinner")==1:
                self.Ux = core.memory("Joueur2").position - self.position
            else:
                self.Ux = core.memory("Joueur1").position - self.position
            self.l = self.Ux.length()
            self.Ux = self.Ux.normalize()
            self.L = abs(self.l - self.l0)
            self.Fx = 0.0004 * self.L * self.Ux
            self.direction = self.direction + self.Fx

        else:
            self.Ux = Vector2(0, 0)


        self.position = self.direction + self.position
