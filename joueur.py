import pygame
from ballon import Ballon
from math import *


class Joueur(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.launchBall = False
        self.velocity = 1
        self.balle = Ballon()
        self.image = pygame.image.load("assets/basketball-player.png")
        self.image = pygame.transform.scale(self.image, (220, 310))
        self.rect = self.image.get_rect()
        self.rect.x = 100
        self.rect.y = 350
        self.balle.setCoords(self.rect.x + self.rect.width - 20, self.rect.y)

    def moveRight(self):
        if self.rect.x < 540 - self.rect.width:
            self.rect.x += self.velocity
            if not self.launchBall:
                self.balle.rect.x += self.velocity

    def moveLeft(self):
        if self.rect.x > 0:
            self.rect.x -= self.velocity
            if not self.launchBall:
                self.balle.rect.x -= self.velocity

    def launch(self):
        self.balle.rect.x += self.balle.velocity
        self.balle.rect.y += self.balle.velocity
