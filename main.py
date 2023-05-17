import pygame

import ManageMenu
import ManageScreen
import Models

pygame.init()
window = pygame.display.set_mode((Models.BOX_WIDTH, Models.BOX_HEIGHT))
pygame.display.set_caption("Menu")

# Chargement des images
pygame.display.set_caption("VollEfrei")
logo = pygame.image.load("assets/logo.png").convert()
icon = pygame.transform.scale(logo, (32, 32))
pygame.display.set_icon(icon)
background_menu_image = pygame.image.load("assets/MENU_DEBUT_PONG.png")
background_menu_image = background_menu_image.convert()

settings_button_image = pygame.image.load("assets/CASE_OPTIONS.png").convert_alpha()
play_button_image = pygame.image.load("assets/CASE_JOUER.png").convert_alpha()
credits_button_image = pygame.image.load("assets/CASE_CREDITS.png").convert_alpha()
quit_button_image = pygame.image.load("assets/CASE_QUITTER.png").convert_alpha()

# Positionnement des boutons
settings_button_rect = settings_button_image.get_rect(center=(Models.BOX_WIDTH//2, 400))
play_button_rect = play_button_image.get_rect(center=(Models.BOX_WIDTH//2, 300))
credits_button_rect = credits_button_image.get_rect(center=(Models.BOX_WIDTH//2, 500))
quit_button_rect = quit_button_image.get_rect(center=(Models.BOX_WIDTH//2, 600))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                if play_button_rect.collidepoint(event.pos):
                    ManageMenu.launchGame(window)
                elif credits_button_rect.collidepoint(event.pos):
                    ManageMenu.launchCredits(window, background_menu_image, quit_button_image, quit_button_rect)
                elif quit_button_rect.collidepoint(event.pos):
                    pygame.quit()
                    exit()
    window.blit(background_menu_image, (0, 0))
    window.blit(play_button_image, play_button_rect)
    window.blit(settings_button_image, settings_button_rect)
    window.blit(credits_button_image, credits_button_rect)
    window.blit(quit_button_image, quit_button_rect)
    pygame.display.update()