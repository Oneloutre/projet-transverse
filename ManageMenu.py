import time
import ManagePlayers
import Models
import pygame
import ManageScreen
import ManageBall


def launchGame(window, background):
    """
    Paramètre 1 : window : fenêtre de jeu
    Paramètre 2 : background : image du fond d'écran du menu
    Fonction permettant de faire tourner le jeu.
    """
    # Charge l'image de fond du jeu
    backgroundGameImage = pygame.image.load("assets/FOND_VOLLEYPONG.png").convert_alpha()

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

        # Vérifie si aucun joueur n'a atteint le score maximum
        if Models.player1["points"] < Models.SCORE_MAX and Models.player2["points"] < Models.SCORE_MAX:
            Player1Rect = pygame.Rect(Models.player1["x"], Models.player1["y"], Models.player1["width"], Models.player1["height"])
            ManageScreen.drawPlayerRect(window, Models.INITIAL_PLAYER_COLOR, Player1Rect)
            player2Rect = pygame.Rect(Models.player2["x"], Models.player2["y"], Models.player2["width"], Models.player2["height"])
            ManageScreen.drawPlayerRect(window, Models.INITIAL_PLAYER_COLOR, player2Rect)

            # Gère le mouvement de la balle
            if Models.ball['timer'] == 0:
                ManageBall.moveBall()
            else:
                ManageScreen.timer3s(window)

            # Dessine la balle
            pygame.draw.circle(window, Models.INITIAL_BALL_COLOR, (Models.ball["x"], Models.ball["y"]),
                               Models.INITIAL_RADIUS)

            # Gère le mouvement des joueurs
            ManagePlayers.move(Models.player1)
            ManagePlayers.move(Models.player2)

            # Affiche le score des joueurs à l'écran
            ManageScreen.displayOnScreen(window, str(Models.player1["points"]) + " - " + str(
                Models.player2["points"]), 500, 0, (255, 255, 255), 100)

            pygame.display.update()  # Met à jour l'affichage de la fenêtre
        else:
            endGame = True
            displayFinalScore(window, backgroundGameImage, background)
            resetSettings()


def displayFinalScore(window, backgroundGameImage, backgroundSettingsImage):
    """
    Paramètre 1 : window: fenêtre de jeu
    Paramètre 2 : backgroundGameImage: Image du fond d'écran du jeu
    Paramètre 3 : backgroundSettingsImage: Image du fond d'écran des options
    Cette fonction permet d'afficher le score final.
    """
    timesleep = 50

    # Boucle pour afficher le score final pendant un certain temps
    while timesleep > 0:
        if Models.player1["points"] == Models.SCORE_MAX:
            # Affiche le message "GAGNANT" pour le joueur 1 en vert
            ManageScreen.displayOnScreen(window, "GAGNANT", 100, 200, (0, 255, 0), 100)
            # Affiche le message "PERDANT" pour le joueur 2 en rouge
            ManageScreen.displayOnScreen(window, "PERDANT", 800, 200, (255, 0, 0), 100)
        else:
            # Affiche le message "GAGNANT" pour le joueur 2 en vert
            ManageScreen.displayOnScreen(window, "GAGNANT", 800, 200, (0, 255, 0), 100)
            # Affiche le message "PERDANT" pour le joueur 1 en rouge
            ManageScreen.displayOnScreen(window, "PERDANT", 100, 200, (255, 0, 0), 100)

        # Affiche le score des joueurs à l'écran
        ManageScreen.displayOnScreen(window, str(Models.player1["points"]) + " - " + str(
            Models.player2["points"]), 500, 0, (255, 255, 255), 100)

        pygame.display.update()  # Met à jour l'affichage de la fenêtre

        keys = pygame.key.get_pressed()

        if keys[pygame.K_ESCAPE]:
            breakInGame(window, backgroundSettingsImage)
            window.blit(backgroundGameImage, (0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        time.sleep(0.1)
        timesleep -= 1


def launchCredits(window, background, quitButton, quitButtonRect):
    """
    Paramètre 1 : window : fenêtre de jeu
    Paramètre 2 : background : Image du fond d'écran du menu
    Paramètre 3 : quitButton : Image du bouton quitter
    Paramètre 4 : quitButtonRect : Rectangle du bouton quitter
    Fonction permettant d'afficher le menu des crédits
    """
    QuitCredit = False

    # Affiche l'arrière-plan et le bouton de quitter
    window.blit(background, (0, 0))
    window.blit(quitButton, quitButtonRect)

    # Affiche les crédits des contributeurs
    ManageScreen.displayOnScreen(window, "Valentin Le Gall", 435, 200, (63, 72, 204), 45)
    ManageScreen.displayOnScreen(window, "Luc Martrenchar", 450, 275, (63, 72, 204), 45)
    ManageScreen.displayOnScreen(window, "Roch Triomphe", 475, 350, (63, 72, 204), 45)
    ManageScreen.displayOnScreen(window, "Mélia Tanguy", 480, 425, (63, 72, 204), 45)
    ManageScreen.displayOnScreen(window, "Alban Sulpice", 465, 500, (63, 72, 204), 45)

    pygame.display.update()  # Met à jour l'affichage de la fenêtre

    while not QuitCredit:
        for event in pygame.event.get():
            keys = pygame.key.get_pressed()

            if (event.type == pygame.QUIT) or (keys[pygame.K_ESCAPE]):
                pygame.quit()
                exit()

            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if quitButtonRect.collidepoint(event.pos):
                        QuitCredit = True


def launchSettings(window, background, quitButton, quitButtonRect):
    """
    Paramètre 1 : window : fenêtre de jeu
    Paramètre 2 : background : Image du fond d'écran du menu
    Paramètre 3 : quitButton : Image du bouton quitter
    Paramètre 4 : quitButtonRect : Rectangle du bouton quitter
    Fonction permettant d'afficher le menu options
    """
    # Initialisation des rectangles et des valeurs de paramètres initiaux
    initialRectPlayer = ManageScreen.returnRectOfPlayer(435, 180)
    dictOfPlayersRects = returnDictOfPlayersRects()
    initialRectBall = ManageScreen.returnRectOfBall(380, 320)
    dictOfBallsRects = returnDictOfBallsRects()
    addDifficultyRect = pygame.Rect(75, 550, 30, 30)
    removeDifficultyRect = pygame.Rect(175, 550, 30, 30)
    addMaxPointRect = pygame.Rect(985, 550, 30, 30)
    removeMaxPointRect = pygame.Rect(1100, 550, 30, 30)
    quitSettings = False

    while not quitSettings:
        window.blit(background, (0, 0))  # Affiche l'arrière-plan
        window.blit(quitButton, quitButtonRect)  # Affiche le bouton de quitter

        # Section de modification de la couleur de la plateforme
        ManageScreen.displayOnScreen(window, "Couleur Plateforme :", 50, 165, "white", 30)
        ManageScreen.drawPlayerRect(window, Models.INITIAL_PLAYER_COLOR, initialRectPlayer)
        ManageScreen.drawDictOfPlayerRect(window, dictOfPlayersRects)

        # Section de modification de la couleur de la balle
        ManageScreen.displayOnScreen(window, "Couleur Balle :", 50, 300, "white", 30)
        ManageScreen.drawBallRect(window, Models.INITIAL_BALL_COLOR, initialRectBall)
        ManageScreen.drawDictOfBallRect(window, dictOfBallsRects)

        # Section de modification de la difficulté
        ManageScreen.displayOnScreen(window, "Difficulty", 50, 500, "white", 30)
        ManageScreen.displayOnScreen(window, "+  " + str(Models.DIFFICULTY) + "  -", 75, 550, "white", 30)

        # Section de modification du score maximum
        ManageScreen.displayOnScreen(window, "Score", 1000, 500, "white", 30)
        ManageScreen.displayOnScreen(window, "+  " + str(Models.SCORE_MAX) + "  -", 985, 550, "white", 30)

        pygame.display.update()  # Met à jour l'affichage de la fenêtre

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Bouton gauche de la souris
                    if quitButtonRect.collidepoint(event.pos):
                        quitSettings = True  # Quitte la boucle et retourne au menu principal
                    if addDifficultyRect.collidepoint(event.pos):
                        if Models.DIFFICULTY < 9:
                            Models.DIFFICULTY += 1  # Incrémente la difficulté
                            Models.INTERVAL = Models.DIFFICULTY * 0.01  # Met à jour l'intervalle de déplacement
                    if removeDifficultyRect.collidepoint(event.pos):
                        if Models.DIFFICULTY > 1:
                            Models.DIFFICULTY -= 1
                            Models.INTERVAL = Models.DIFFICULTY * 0.01
                    if addMaxPointRect.collidepoint(event.pos):
                        Models.SCORE_MAX += 1  # Incrémente le score maximum
                        # Met à jour la position du rectangle de suppression du score maximum
                        removeMaxPointRect = pygame.Rect(1050 + (len(str(Models.SCORE_MAX)) * 30), 550, 30, 30)
                    if removeMaxPointRect.collidepoint(event.pos):
                        if Models.SCORE_MAX > max(Models.player1["points"], Models.player2["points"]) + 1:
                            Models.SCORE_MAX -= 1  # Décrémente le score maximum
                        # Met à jour la position du rectangle de suppression du score maximum
                        removeMaxPointRect = pygame.Rect(1080 + (len(str(Models.SCORE_MAX)) * 15), 550, 30, 30)
                    collisionToSwitchPlayerColorWithDict(dictOfPlayersRects, event.pos)
                    collisionToSwitchBallColorWithDict(dictOfBallsRects, event.pos)


def returnDictOfPlayersRects():
    """
    La fonction returnDictOfPlayersRects() retourne un dictionnaire
    contenant des rectangles de couleurs pour les plateformes des joueurs.
    """
    # Création des rectangles de couleur pour chaque plateforme de joueur
    RedRectPlayer = ManageScreen.returnRectOfPlayer(100, 225)
    BlueRectPlayer = ManageScreen.returnRectOfPlayer(250, 225)
    OrangeRectPlayer = ManageScreen.returnRectOfPlayer(400, 225)
    YellowRectPlayer = ManageScreen.returnRectOfPlayer(550, 225)
    GreenRectPlayer = ManageScreen.returnRectOfPlayer(700, 225)
    WhiteRectPlayer = ManageScreen.returnRectOfPlayer(850, 225)
    PurpleRectPlayer = ManageScreen.returnRectOfPlayer(1000, 225)

    # Création du dictionnaire contenant les rectangles de couleur pour chaque plateforme
    dictOfPlayersRects = {'red': RedRectPlayer, 'blue': BlueRectPlayer, 'orange': OrangeRectPlayer,
                          'yellow': YellowRectPlayer, 'green': GreenRectPlayer, 'white': WhiteRectPlayer,
                          'purple': PurpleRectPlayer}

    # Retourne le dictionnaire de rectangles de couleur des plateformes
    return dictOfPlayersRects


def returnDictOfBallsRects():
    """
    La fonction returnDictOfBallsRects() retourne un dictionnaire
    contenant les rectangles des balles de différentes couleurs.
    """
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
    """
    La fonction collisionToSwitchPlayerColor(Rect, color, event) vérifie si un événement de souris (clic) se produit sur
    le rectangle spécifié. Si c'est le cas, elle met à jour la couleur initiale du joueur avec la couleur fournie.
    """
    # Vérifie si le rectangle spécifié est en collision avec l'événement de souris
    if Rect.collidepoint(event):
        # Met à jour la couleur initiale du joueur avec la couleur fournie
        Models.INITIAL_PLAYER_COLOR = color


def collisionToSwitchPlayerColorWithDict(dictOfPlayersRects, event):
    """
    Paramètre 1 : dictOfPlayersRects: dictionnaire des plateforme affichées au menu.
    Paramètre 2 : event: évènement (clique de la souris)
    La fonction collisionToSwitchPlayerColorWithDict(dictOfPlayersRects, event) itère sur les différentes couleurs du
    dictionnaire dictOfPlayersRects et applique la fonction collisionToSwitchPlayerColor pour chaque couleur.
    """
    # Parcourt les différentes couleurs du dictionnaire
    for color in dictOfPlayersRects.keys():
        # Applique la fonction collisionToSwitchPlayerColor pour chaque couleur
        collisionToSwitchPlayerColor(dictOfPlayersRects[color], color, event)


def collisionToSwitchBallColor(Rect, color, event):
    """
    Paramètre 1 : Rect: rectangle spécifique d'une balle affichée dans le menu.
    Paramètre 2 : color: couleur de la balle en question.
    Paramètre 3 : event: évènement (clique de la souris).
    La fonction collisionToSwitchBallColor(Rect, color, event) vérifie si le rectangle Rect est en collision avec
    l'événement event et si c'est le cas, elle met à jour la couleur de la balle en utilisant la couleur color.
    """
    # Vérifie si le rectangle est en collision avec l'événement
    if Rect.collidepoint(event):
        # Met à jour la couleur de la balle avec la couleur spécifiée
        Models.INITIAL_BALL_COLOR = color


def collisionToSwitchBallColorWithDict(dictOfBallsRects, event):
    """
    Paramètre 1 : dictOfBallsRects: dictionnaire des balles affichées au menu.
    Paramètre 2 : event: évènement (clique de la souris)
    La fonction collisionToSwitchBallColorWithDict(dictOfBallsRects, event) itère à travers les clés du dictionnaire
    dictOfBallsRects et appelle la fonction collisionToSwitchBallColor pour chaque clé. Elle permet de vérifier la
    collision entre l'événement de souris et les rectangles de couleur associés à la balle et met à jour la couleur de
    la balle en conséquence.
    """
    # Itère à travers les clés du dictionnaire
    for color in dictOfBallsRects.keys():
        # Appelle la fonction collisionToSwitchBallColor pour chaque clé
        collisionToSwitchBallColor(dictOfBallsRects[color], color, event)


def resetSettings():
    """
    La fonction resetSettings() est utilisée pour réinitialiser les paramètres du jeu.
    """
    # Réinitialise la position de la balle avec les valeurs initiales
    ManageBall.placeBall(Models.INITIAL_X, Models.INITIAL_Y, Models.INITIAL_ANGLE)

    # Réinitialise les paramètres du joueur 1 avec les valeurs initiales
    Models.player1 = {"points": 0, "x": 200, "y": 500, "width": 100, "height": 10, "move": 0}

    # Réinitialise les paramètres du joueur 2 avec les valeurs initiales
    Models.player2 = {"points": 0, "x": 1000, "y": 500, "width": 100, "height": 10, "move": 0}


def breakInGame(window, background):
    """
    :param window: fenêtre du jeu
    :param background: image du fond d'écran du menu pause
    La fonction breakInGame(window, background) est utilisée pour
    faire une pause dans le jeu et afficher un menu de pause.
    """
    # Chargement des images des boutons de quit, resume et settings
    quitButton = pygame.image.load("assets/CASE_QUITTER.png").convert_alpha()
    quitButtonRect = quitButton.get_rect(center=(Models.BOX_WIDTH // 2, 600))
    resumeButton = pygame.image.load("assets/CASE_REPRENDRE.png").convert_alpha()
    resumeButtonRect = resumeButton.get_rect(center=(Models.BOX_WIDTH // 2, 400))
    settingsButton = pygame.image.load("assets/CASE_OPTIONS.png").convert_alpha()
    settingsButtonRect = settingsButton.get_rect(center=(Models.BOX_WIDTH // 2, 500))

    quitBreak = False
    while not quitBreak:
        window.blit(background, (0, 0))
        window.blit(quitButton, quitButtonRect)
        window.blit(settingsButton, settingsButtonRect)
        window.blit(resumeButton, resumeButtonRect)

        # Affichage du score en haut de l'écran
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
                if event.button == 1:
                    if quitButtonRect.collidepoint(event.pos):
                        pygame.quit()
                        exit()
                    if resumeButtonRect.collidepoint(event.pos):
                        quitBreak = True
                    if settingsButtonRect.collidepoint(event.pos):
                        launchSettings(window, background, quitButton, quitButtonRect)
