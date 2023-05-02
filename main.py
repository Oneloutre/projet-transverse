import pygame

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

player1_x = 200
player1_y = 400
player1_is_jumping = False

player2_x = 1000
player2_y = 400
player2_is_jumping = False

players_jump_speed = 1
players_jump_height = 200
players_speed = 1


# Boucle principale du jeu
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                quit()
    keys = pygame.key.get_pressed()
    if keys[pygame.K_q] and player1_x > 40:
        player1_x -= players_speed
    if keys[pygame.K_d] and player1_x < 525:
        player1_x += players_speed
    if keys[pygame.K_LEFT] and player2_x > 650:
        player2_x -= players_speed
    if keys[pygame.K_RIGHT] and player2_x < 1175:
        player2_x += players_speed
    if keys[pygame.K_z] and player1_y == 400:
        player1_is_jumping = True
    if keys[pygame.K_UP] and player2_y == 400:
        player2_is_jumping = True

    if player1_is_jumping and player1_y > 400-players_jump_height:
        player1_y -= players_jump_speed
    elif player1_y < 400:
        player1_is_jumping = False
        player1_y += players_jump_speed

    if player2_is_jumping and player2_y > 400-players_jump_height:
        player2_y -= players_jump_speed
    elif player2_y < 400:
        player2_is_jumping = False
        player2_y += players_jump_speed

    window.blit(background_image, (0, 0))
    pygame.draw.rect(window, 255, pygame.Rect(player1_x, player1_y, 100, 200))
    pygame.draw.rect(window, 255, pygame.Rect(player2_x, player2_y, 100, 200))
    pygame.display.update()
