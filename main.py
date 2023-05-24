import pygame
import ManageMenu
import Models

import pygame

pygame.init()  # Initialise Pygame

# Crée une fenêtre graphique avec une taille définie
window = pygame.display.set_mode((Models.BOX_WIDTH, Models.BOX_HEIGHT))

# Définit le titre de la fenêtre
pygame.display.set_caption("Menu")

# Charge et définit le logo de la fenêtre
pygame.display.set_caption("VollEfrei")
logo = pygame.image.load("assets/logo.png").convert()
icon = pygame.transform.scale(logo, (32, 32))
pygame.display.set_icon(icon)

# Charge une image de fond pour le menu
background_menu_image = pygame.image.load("assets/MENU_DEBUT_PONG.png").convert()

# Charge les images des différents boutons du menu
settings_button_image = pygame.image.load("assets/CASE_OPTIONS.png").convert_alpha()
play_button_image = pygame.image.load("assets/CASE_JOUER.png").convert_alpha()
credits_button_image = pygame.image.load("assets/CASE_CREDITS.png").convert_alpha()
quit_button_image = pygame.image.load("assets/CASE_QUITTER.png").convert_alpha()

# Définit les positions des différents boutons sur la fenêtre
settings_button_rect = settings_button_image.get_rect(center=(Models.BOX_WIDTH // 2, 400))
play_button_rect = play_button_image.get_rect(center=(Models.BOX_WIDTH // 2, 300))
credits_button_rect = credits_button_image.get_rect(center=(Models.BOX_WIDTH // 2, 500))
quit_button_rect = quit_button_image.get_rect(center=(Models.BOX_WIDTH // 2, 600))

while True:
    for event in pygame.event.get():
        keys = pygame.key.get_pressed()

        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                # Vérifie si le bouton "Jouer" a été cliqué
                if play_button_rect.collidepoint(event.pos):
                    ManageMenu.launchGame(window, background_menu_image)

                # Vérifie si le bouton "Crédits" a été cliqué
                elif credits_button_rect.collidepoint(event.pos):
                    ManageMenu.launchCredits(window, background_menu_image, quit_button_image, quit_button_rect)

                # Vérifie si le bouton "Options" a été cliqué
                elif settings_button_rect.collidepoint(event.pos):
                    ManageMenu.launchSettings(window, background_menu_image, quit_button_image, quit_button_rect)

                # Vérifie si le bouton "Quitter" a été cliqué
                elif quit_button_rect.collidepoint(event.pos):
                    pygame.quit()
                    exit()

    # Affiche l'image de fond du menu
    window.blit(background_menu_image, (0, 0))

    # Affiche les différents boutons du menu
    window.blit(play_button_image, play_button_rect)
    window.blit(settings_button_image, settings_button_rect)
    window.blit(credits_button_image, credits_button_rect)
    window.blit(quit_button_image, quit_button_rect)

    pygame.display.update()  # Met à jour l'affichage de la fenêtre
