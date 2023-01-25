import pygame


class Ballon(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.velocity = 1
        self.image = pygame.image.load("assets/basketball.png")
        self.image = pygame.transform.scale(self.image, (60, 60))
        self.rect = self.image.get_rect()
        self.rect.x = 100
        self.rect.y = 100

    def setCoords(self, x, y):
        self.rect.x = x
        self.rect.y = y
