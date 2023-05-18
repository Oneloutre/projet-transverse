import pygame
import Models


def displayOnScreen(window, text, x, y, color, police):
    window.blit(pygame.font.SysFont("monospace", police).render(text, True, color), (x, y))


def timer3s(window):
    if Models.ball['timer'] >= 2 * (Models.INITIAL_TIMER / 3):
        displayOnScreen(window, "3", 590, 160, (255, 255, 255), 200)
    elif Models.ball['timer'] >= (Models.INITIAL_TIMER / 3):
        displayOnScreen(window, "2", 590, 160, (255, 255, 255), 200)
    else:
        displayOnScreen(window, "1", 590, 160, (255, 255, 255), 200)
    Models.ball['timer'] -= 1


def drawPlayerRect(window, color, rect):
    pygame.draw.rect(window, color, rect)


def drawDictOfPlayerRect(window, dict):
    for color in dict.keys():
        drawPlayerRect(window, color, dict[color])


def returnRectOfPlayer(x, y):
    return pygame.Rect(x, y, Models.player1["width"], Models.player1["height"])


def returnRectOfBall(x, y):
    return pygame.Rect(x - Models.ball['radius'], y - Models.ball['radius'],
                       2 * Models.ball['radius'], 2 * Models.ball['radius'])


def drawBallRect(window, color, rect):
    pygame.draw.circle(window, color, (rect.left + Models.ball['radius'], rect.top + Models.ball['radius']),
                       Models.INITIAL_RADIUS)


def drawDictOfBallRect(window, dict):
    for color in dict.keys():
        drawBallRect(window, color, dict[color])
