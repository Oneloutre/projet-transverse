import pygame
import ManagePlayers
import ManageScreen
import ManageBall
import Models
import time

pygame.init()
menu = pygame.display.set_mode((Models.BOX_WIDTH, Models.BOX_HEIGHT))
pygame.display.set_caption("Menu")

# Chargement des images
pygame.display.set_caption("VollEfrei")
logo = pygame.image.load("assets/logo.png").convert()
icon = pygame.transform.scale(logo, (32, 32))
pygame.display.set_icon(icon)

background_menu_image = pygame.image.load("assets/MENU_DEBUT_PONG.png")
background_menu_image = background_menu_image.convert()
play_button_image = pygame.image.load("assets/CASE_JOUER.png").convert_alpha()
credits_button_image = pygame.image.load("assets/CASE_CREDITS.png").convert_alpha()
quit_button_image = pygame.image.load("assets/CASE_QUITTER.png").convert_alpha()

# Positionnement des boutons
play_button_rect = play_button_image.get_rect(center=(Models.BOX_WIDTH//2, 300))
credits_button_rect = credits_button_image.get_rect(center=(Models.BOX_WIDTH//2, 450))
quit_button_rect = quit_button_image.get_rect(center=(Models.BOX_WIDTH//2, 600))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # Bouton gauche de la souris
                if play_button_rect.collidepoint(event.pos):
                    window = pygame.display.set_mode((Models.BOX_WIDTH, Models.BOX_HEIGHT))
                    background_image = pygame.image.load("assets/FOND_VOLLEYPONG.png")
                    background_image = background_image.convert()
                    Models.QUIT = False
                    while not Models.QUIT:
                        ManageScreen.leave()
                        window.blit(background_image, (0, 0))
                        if Models.player1["points"] < Models.SCORE_MAX and Models.player2["points"] < Models.SCORE_MAX:
                            pygame.draw.rect(window, (255, 0, 0),
                                             pygame.Rect(Models.player1["x"], Models.player1["y"],
                                                         Models.player1["width"],
                                                         Models.player1["height"]))
                            pygame.draw.rect(window, (255, 0, 0),
                                             pygame.Rect(Models.player2["x"], Models.player2["y"],
                                                         Models.player2["width"],
                                                         Models.player2["height"]))
                            if Models.ball['timer'] == 0:
                                ManageBall.moveBall()
                            else:
                                ManageScreen.timer3s(window)
                            pygame.draw.circle(window, 255, (Models.ball["x"], Models.ball["y"]),
                                               Models.INITIAL_RADIUS)
                            ManagePlayers.move(Models.player1)
                            ManagePlayers.move(Models.player2)
                        else:
                            ManageScreen.displayFinalScore(window)
                            time.sleep(5)
                            Models.QUIT = True
                        ManageScreen.displayOnScreen(window, str(Models.player1["points"]) + " - " + str(
                            Models.player2["points"]), 500, 0,
                                                     (255, 255, 255), 100)
                        pygame.display.update()

                elif credits_button_rect.collidepoint(event.pos):
                    # Afficher la fenêtre des crédits pendant 10 secondes
                    QuitCredit = False
                    while not QuitCredit:
                        for event in pygame.event.get():
                            if event.type == pygame.MOUSEBUTTONDOWN:
                                if event.button == 1:  # Bouton gauche de la souris
                                    if quit_button_rect.collidepoint(event.pos):
                                        QuitCredit = True
                        menu.blit(background_menu_image, (0, 0))
                        menu.blit(quit_button_image, quit_button_rect)
                        ManageScreen.displayOnScreen(menu, "Valentin Le Gall", 435, 200, (63,72,204), 45)
                        ManageScreen.displayOnScreen(menu, "Luc Martrenchar", 450, 275, (63,72,204), 45)
                        ManageScreen.displayOnScreen(menu, "Roch Triomphe", 475, 350, (63,72,204), 45)
                        ManageScreen.displayOnScreen(menu, "Mélia Tanguy", 480, 425, (63,72,204), 45)
                        ManageScreen.displayOnScreen(menu, "Alban Sulpice", 465, 500, (63,72,204), 45)
                        ManageScreen.leave()
                        pygame.display.update()
                elif quit_button_rect.collidepoint(event.pos):
                    running = False

    menu.blit(background_menu_image, (0, 0))
    menu.blit(play_button_image, play_button_rect)
    menu.blit(credits_button_image, credits_button_rect)
    menu.blit(quit_button_image, quit_button_rect)
    pygame.display.update()

pygame.quit()