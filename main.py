import pygame
from game import Game
from math import *
pygame.init()

pygame.display.set_icon(pygame.image.load("assets/basketball.png"))
pygame.display.set_caption("Basketball Versus")
screen = pygame.display.set_mode((1080, 720))
backgroud = pygame.image.load("assets/demiterrain.png")
running = True
game = Game()
while running:
    screen.blit(backgroud, backgroud.get_rect())
    screen.blit(game.joueur.balle.image, game.joueur.balle.rect)
    screen.blit(game.joueur.image, game.joueur.rect)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
        if event.type == pygame.KEYDOWN:
            game.keyPressed[event.key] = True
            if event.key == pygame.K_SPACE:
                game.joueur.launchBall = True
        if event.type == pygame.KEYUP:
            game.keyPressed[event.key] = False
    if game.keyPressed.get(pygame.K_d):
        game.joueur.moveRight()
    if game.keyPressed.get(pygame.K_q):
        game.joueur.moveLeft()
    if game.joueur.launchBall:
        game.joueur.launch()
    pygame.display.flip()
