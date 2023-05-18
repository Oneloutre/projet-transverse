import time
import ManagePlayers
import Models
import pygame
import ManageScreen
import ManageBall


def launchGame(window, background):
    backgroundGameImage = pygame.image.load("assets/FOND_VOLLEYPONG.png").convert_alpha()
    resetSettings()
    endGame = False
    while not endGame:
        for event in pygame.event.get():
            keys = pygame.key.get_pressed()
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if keys[pygame.K_ESCAPE]:
                breakInGame(window, background)
        window.blit(backgroundGameImage, (0, 0))
        if Models.player1["points"] < Models.SCORE_MAX and Models.player2["points"] < Models.SCORE_MAX:
            pygame.draw.rect(window, Models.INITIAL_PLAYER_COLOR,
                             pygame.Rect(Models.player1["x"], Models.player1["y"],
                                         Models.player1["width"],
                                         Models.player1["height"]))
            pygame.draw.rect(window, Models.INITIAL_PLAYER_COLOR,
                             pygame.Rect(Models.player2["x"], Models.player2["y"],
                                         Models.player2["width"],
                                         Models.player2["height"]))
            if Models.ball['timer'] == 0:
                ManageBall.moveBall()
            else:
                ManageScreen.timer3s(window)
            pygame.draw.circle(window, Models.ball["color"], (Models.ball["x"], Models.ball["y"]),
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
            ManageScreen.timesleep(50)
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
            keys = pygame.key.get_pressed()
            if (event.type == pygame.QUIT) or (keys[pygame.K_ESCAPE]):
                pygame.quit()
                exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Bouton gauche de la souris

                    if quitButtonRect.collidepoint(event.pos):
                        QuitCredit = True


def launchSettings(window, background, quitButton, quitButtonRect):
    initialRectPlayer = ManageScreen.returnRectOfPlayer(350, 165)
    dictOfPlayersRects = returnDictOfPlayersRects()
    initialRectBall = ManageScreen.returnRectOfBall(320, 320)
    dictOfBallsRects = returnDictOfBallsRects()
    addDifficultyRect = pygame.Rect(75, 550, 30, 30)
    removeDifficultyRect = pygame.Rect(175, 550, 30, 30)
    addMaxPointRect = pygame.Rect(985, 550, 30, 30)
    removeMaxPointRect = pygame.Rect(1100, 550, 30, 30)
    quitSettings = False
    while not quitSettings:
        window.blit(background, (0, 0))
        window.blit(quitButton, quitButtonRect)
        ManageScreen.displayOnScreen(window, "Platform Color:", 50, 150, "white", 30)
        ManageScreen.drawPlayerRect(window, Models.INITIAL_PLAYER_COLOR, initialRectPlayer)
        ManageScreen.drawDictOfPlayerRect(window, dictOfPlayersRects)
        ManageScreen.displayOnScreen(window, "Ball Color:", 50, 300, "white", 30)
        ManageScreen.drawBallRect(window, Models.INITIAL_BALL_COLOR, initialRectBall)
        ManageScreen.drawDictOfBallRect(window, dictOfBallsRects)
        ManageScreen.displayOnScreen(window, "Difficulty", 50, 500, "white", 30)
        ManageScreen.displayOnScreen(window, "+  " + str(Models.DIFFICULTY) + "  -", 75, 550, "white", 30)
        ManageScreen.displayOnScreen(window, "Score", 1000, 500, "white", 30)
        ManageScreen.displayOnScreen(window, "+  " + str(Models.SCORE_MAX) + "  -", 985, 550, "white", 30)
        pygame.display.update()
        for event in pygame.event.get():
            keys = pygame.key.get_pressed()
            if (event.type == pygame.QUIT) or (keys[pygame.K_ESCAPE]):
                pygame.quit()
                exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Bouton gauche de la souris
                    if quitButtonRect.collidepoint(event.pos):
                        quitSettings = True
                    if addDifficultyRect.collidepoint(event.pos):
                        if Models.DIFFICULTY < 9:
                            Models.DIFFICULTY += 1
                            Models.INTERVAL = Models.DIFFICULTY * 0.01
                    if removeDifficultyRect.collidepoint(event.pos):
                        if Models.DIFFICULTY > 1:
                            Models.DIFFICULTY -= 1
                            Models.INTERVAL = Models.DIFFICULTY * 0.01
                    if addMaxPointRect.collidepoint(event.pos):
                        Models.SCORE_MAX += 1
                    if removeMaxPointRect.collidepoint(event.pos):
                        if Models.SCORE_MAX > 0:
                            Models.SCORE_MAX -= 1
                    collisionToSwitchPlayerColorWithDict(dictOfPlayersRects, event.pos)
                    collisionToSwitchBallColorWithDict(dictOfBallsRects, event.pos)


def returnDictOfPlayersRects():
    RedRectPlayer = ManageScreen.returnRectOfPlayer(100, 225)
    BlueRectPlayer = ManageScreen.returnRectOfPlayer(250, 225)
    OrangeRectPlayer = ManageScreen.returnRectOfPlayer(400, 225)
    YellowRectPlayer = ManageScreen.returnRectOfPlayer(550, 225)
    GreenRectPlayer = ManageScreen.returnRectOfPlayer(700, 225)
    WhiteRectPlayer = ManageScreen.returnRectOfPlayer(850, 225)
    PurpleRectPlayer = ManageScreen.returnRectOfPlayer(1000, 225)
    dictOfPlayersRects = {'red': RedRectPlayer, 'blue': BlueRectPlayer, 'orange': OrangeRectPlayer,
                          'Yellow': YellowRectPlayer, 'green': GreenRectPlayer, 'white': WhiteRectPlayer,
                          'purple': PurpleRectPlayer}
    return dictOfPlayersRects


def returnDictOfBallsRects():
    RedRectBall = ManageScreen.returnRectOfBall(150, 400)
    BlueRectBall = ManageScreen.returnRectOfBall(300, 400)
    OrangeRectBall = ManageScreen.returnRectOfBall(450, 400)
    YellowRectBall = ManageScreen.returnRectOfBall(600, 400)
    GreenRectBall = ManageScreen.returnRectOfBall(750, 400)
    WhiteRectBall = ManageScreen.returnRectOfBall(900, 400)
    PurpleRectBall = ManageScreen.returnRectOfBall(1050, 400)
    dictOfBallsRects = {'red': RedRectBall, 'blue': BlueRectBall, 'orange': OrangeRectBall,
                        'Yellow': YellowRectBall, 'green': GreenRectBall, 'white': WhiteRectBall,
                        'purple': PurpleRectBall}
    return dictOfBallsRects


def collisionToSwitchPlayerColor(Rect, color, event):
    if Rect.collidepoint(event):
        Models.INITIAL_PLAYER_COLOR = color


def collisionToSwitchPlayerColorWithDict(dictOfPlayersRects, event):
    for color in dictOfPlayersRects.keys():
        collisionToSwitchPlayerColor(dictOfPlayersRects[color], color, event)


def collisionToSwitchBallColor(Rect, color, event):
    if Rect.collidepoint(event):
        Models.INITIAL_BALL_COLOR = color


def collisionToSwitchBallColorWithDict(dictOfBallsRects, event):
    for color in dictOfBallsRects.keys():
        collisionToSwitchBallColor(dictOfBallsRects[color], color, event)


def resetSettings():
    ManageBall.placeBall(Models.INITIAL_X, Models.INITIAL_Y, Models.INITIAL_ANGLE)
    Models.player1 = {"points": 0, "x": 200, "y": 500, "width": 100, "height": 10, "move": 0}
    Models.player2 = {"points": 0, "x": 1000, "y": 500, "width": 100, "height": 10, "move": 0}


def breakInGame(window, background):
    quitButton = pygame.image.load("assets/CASE_QUITTER.png").convert_alpha()
    quitButtonRect = quitButton.get_rect(center=(Models.BOX_WIDTH // 2, 600))
    quitBreak = False
    while not quitBreak:
        window.blit(background, (0, 0))
        window.blit(quitButton, quitButtonRect)
        ManageScreen.displayOnScreen(window, str(Models.player1["points"]) + " - " + str(
            Models.player2["points"]), 420, 200, (255, 255, 255), 150)
        pygame.display.update()
        for event in pygame.event.get():
            keys = pygame.key.get_pressed()
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if keys[pygame.K_ESCAPE]:
                quitBreak = True
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Bouton gauche de la souris
                    if quitButtonRect.collidepoint(event.pos):
                        pygame.quit()
                        exit()

