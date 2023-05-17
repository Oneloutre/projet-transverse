import pygame

import Models



def displayOnScreen(window, text, x, y, color, police):
    window.blit(pygame.font.SysFont("monospace", police).render(text, True, color), (x, y))


def timer3s(window):
    if Models.ball['timer'] >= 2*(Models.INITIAL_TIMER/3):
        displayOnScreen(window, "3", 590, 160, (255, 255, 255), 200)
    elif Models.ball['timer'] >= (Models.INITIAL_TIMER/3):
        displayOnScreen(window, "2", 590, 160, (255, 255, 255), 200)
    else:
        displayOnScreen(window, "1", 590, 160, (255, 255, 255), 200)
    Models.ball['timer'] -= 1

def displayFinalScore(window):
    if Models.player1["points"] == Models.SCORE_MAX:
        displayOnScreen(window, "Joueur 1 a gagné !", 100, 200, (255, 0, 0), 100)
    else:
        displayOnScreen(window, "Joueur 2 a gagné !", 100, 200, (255, 0, 0), 100)