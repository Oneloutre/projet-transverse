import math

import pygame
import ManagePlayers
import ManageScreen
import ManageBall
import Models
import time

pygame.init()
window = pygame.display.set_mode((Models.BOX_WIDTH, Models.BOX_HEIGHT))
pygame.display.set_caption("VollEfrei")
# logo = pygame.image.load("assets/logo.png")
# pygame.display.set_icon(logo)
background_image = pygame.image.load("assets/FOND_VOLLEYPONG.png")
background_image = background_image.convert()

while Models.player1["points"] < Models.SCORE_MAX and Models.player2["points"] < Models.SCORE_MAX:
    ManageScreen.leave()
    window.blit(background_image, (0, 0))
    scoreBoard = pygame.font.SysFont("monospace", 100).render(
        str(Models.player1["points"]) + " - " + str(Models.player2["points"]), True, (255, 255, 255))
    window.blit(scoreBoard, (500, 0))
    pygame.draw.rect(window, (255, 0, 0), pygame.Rect(Models.player1["x"], Models.player1["y"], Models.player1["width"],
                                                      Models.player1["height"]))
    pygame.draw.rect(window, (255, 0, 0), pygame.Rect(Models.player2["x"], Models.player2["y"], Models.player2["width"],
                                                      Models.player2["height"]))
    if Models.ball['visible']:
        ManageBall.moveBall()
        pygame.draw.circle(window, 255, (Models.ball["x"], Models.ball["y"]),
                           Models.INITIAL_RADIUS)
    ManagePlayers.move(Models.player1, Models.playersParameters)
    ManagePlayers.move(Models.player2, Models.playersParameters)
    pygame.display.update()
if Models.player1["points"] == Models.SCORE_MAX:
    Result = pygame.font.SysFont("monospace", 100).render("Joueur 1 a gagné !", True, (255, 0, 0))
else:
    Result = pygame.font.SysFont("monospace", 100).render("Joueur 2 a gagné !", True, (255, 0, 0))
scoreBoard = pygame.font.SysFont("monospace", 100).render(
        str(Models.player1["points"]) + " - " + str(Models.player2["points"]), True, (255, 255, 255))
window.blit(Result, (120, 400))
pygame.display.update()
time.sleep(5)