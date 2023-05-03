import pygame
import ManagePlayers
import ManageScreen

# Initialisation de Pygame
pygame.init()

# Définition des dimensions de la fenêtre
window_width = 1280
window_height = 720

# Création de la fenêtre avec le titre "VollEfrei"
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("VollEfrei")

# Chargement de l'image du logo
logo = pygame.image.load("assets/logo.png")

# Définition du logo de la fenêtre
pygame.display.set_icon(logo)

# Chargement de l'image de fond
background_image = pygame.image.load("assets/background.png")
background_image = background_image.convert()


player1 = {"x": 200, "y": 300, "jumping": False}
player2 = {"x": 1000, "y": 300, "jumping": False}

playersParameters = {"speed": 1, "jumpSpeed": 1, "jumpHeight": 200}

player1Image = pygame.image.load("assets/spritePlayer.png").convert_alpha()
player2Image = pygame.transform.flip(player1Image, True, False)
# playerImage = pygame.transform.scale(playerImage, (100, 200))


# Boucle principale du jeu
while True:

    ManageScreen.leave()
    ManagePlayers.move(player1, playersParameters)
    ManagePlayers.move(player2, playersParameters)
    ManagePlayers.jump(player1, playersParameters)
    ManagePlayers.jump(player2, playersParameters)

    window.blit(background_image, (0, 0))
    window.blit(player1Image, (player1["x"], player1["y"]))
    window.blit(player2Image, (player2["x"], player2["y"]))
    pygame.display.update()
