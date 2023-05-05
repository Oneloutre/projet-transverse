import pygame
import ManagePlayers
import ManageScreen
import math
import ManageBall
import Models

# Initialisation de Pygame
pygame.init()

# Création de la fenêtre avec le titre "VollEfrei"
window = pygame.display.set_mode((Models.window_width, Models.window_height))
pygame.display.set_caption("VollEfrei")

# Chargement de l'image du logo
logo = pygame.image.load("assets/logo.png")

# Définition du logo de la fenêtre
pygame.display.set_icon(logo)

# Chargement de l'image de fond
background_image = pygame.image.load("assets/background.png")
background_image = background_image.convert()

player1Image = pygame.image.load("assets/spritePlayer.png").convert_alpha()
player2Image = pygame.transform.flip(player1Image, True, False)


while True:

    ManageScreen.leave()
    
    ManagePlayers.move(Models.player1, Models.playersParameters)
    ManagePlayers.move(Models.player2, Models.playersParameters)
    ManagePlayers.jump(Models.player1, Models.playersParameters)
    ManagePlayers.jump(Models.player2, Models.playersParameters)
    window.blit(background_image, (0, 0))
    window.blit(player1Image, (Models.player1["x"], Models.player1["y"]))
    window.blit(player2Image, (Models.player2["x"], Models.player2["y"]))
    if Models.ball['visible']:
        ManageBall.moveBall()
        pygame.draw.circle(window, 255, (Models.ball["x"], Models.ball["y"] - 2 * Models.ball["radius"]),
                           Models.INITIAL_RADIUS)

    pygame.display.update()

