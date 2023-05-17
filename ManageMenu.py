import time
import ManagePlayers
import Models
import pygame
import ManageScreen
import ManageBall


def launchGame(window):
    background_image = pygame.image.load("assets/FOND_VOLLEYPONG.png")
    background_image = background_image.convert()
    endGame = False
    while not endGame:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
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
            ManageScreen.displayOnScreen(window, str(Models.player1["points"]) + " - " + str(
                Models.player2["points"]), 500, 0, (255, 255, 255), 100)
            pygame.display.update()
        else:
            ManageScreen.displayFinalScore(window)
            ManageScreen.displayOnScreen(window, str(Models.player1["points"]) + " - " + str(
                Models.player2["points"]), 500, 0, (255, 255, 255), 100)
            pygame.display.update()
            time.sleep(5)
            resetSettings()
            endGame = True


def launchCredits(window, background, quitButton, quitButtonRect):
    QuitCredit = False
    while not QuitCredit:
        window.blit(background, (0, 0))
        window.blit(quitButton, quitButtonRect)
        ManageScreen.displayOnScreen(window, "Valentin Le Gall", 435, 200, (63, 72, 204), 45)
        ManageScreen.displayOnScreen(window, "Luc Martrenchar", 450, 275, (63, 72, 204), 45)
        ManageScreen.displayOnScreen(window, "Roch Triomphe", 475, 350, (63, 72, 204), 45)
        ManageScreen.displayOnScreen(window, "Mélia Tanguy", 480, 425, (63, 72, 204), 45)
        ManageScreen.displayOnScreen(window, "Alban Sulpice", 465, 500, (63, 72, 204), 45)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Bouton gauche de la souris
                    if quitButtonRect.collidepoint(event.pos):
                        QuitCredit = True

def resetSettings():
    ManageBall.placeBall(Models.INITIAL_X, Models.INITIAL_Y, Models.INITIAL_ANGLE)
    Models.player1 = {"points": 0, "x": 200, "y": 500, "width": 100, "height": 10}
    Models.player2 = {"points": 0, "x": 1000, "y": 500, "width": 100, "height": 10}