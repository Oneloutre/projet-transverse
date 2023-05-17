import pygame
import ManagePlayers
import ManageScreen
import ManageBall
import Models

pygame.init()
window = pygame.display.set_mode((Models.BOX_WIDTH, Models.BOX_HEIGHT))
pygame.display.set_caption("VollEfrei")
logo = pygame.image.load("assets/logo.png").convert()
icon = pygame.transform.scale(logo, (32, 32))
pygame.display.set_icon(icon)
background_image = pygame.image.load("assets/FOND_VOLLEYPONG.png")
background_image = background_image.convert()

while not Models.QUIT:
    if Models.MENU:
        pass
    else:
        ManageScreen.leave()
        window.blit(background_image, (0, 0))
        if Models.player1["points"] < Models.SCORE_MAX and Models.player2["points"] < Models.SCORE_MAX:
            pygame.draw.rect(window, (255, 0, 0), pygame.Rect(Models.player1["x"], Models.player1["y"], Models.player1["width"],
                                                              Models.player1["height"]))
            pygame.draw.rect(window, (255, 0, 0), pygame.Rect(Models.player2["x"], Models.player2["y"], Models.player2["width"],
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
        ManageScreen.displayOnScreen(window, str(Models.player1["points"]) + " - " + str(Models.player2["points"]), 500, 0,
                                     (255, 255, 255), 100)
        Models.MENU = True
    pygame.display.update()