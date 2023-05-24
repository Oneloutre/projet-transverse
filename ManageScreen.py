import pygame
import Models


def displayOnScreen(window, text, x, y, color, police):
    """
    Paramètre 1 : window : fenêtre du jeu.
    Paramètre 1 : text : texte que l'on veut écrire.
    Paramètre 1 : x : Position x du texte.
    Paramètre 1 : y : Position y du texte.
    Paramètre 1 : color : Couleur du texte
    Paramètre 1 : police : Taille du texte
    La fonction displayOnScreen(window, text, x, y, color, police) est
    utilisée pour afficher du texte à l'écran dans une fenêtre spécifiée.
    """
    window.blit(pygame.font.SysFont("monospace", police).render(text, True, color), (x, y))


def timer3s(window):
    """
    Paramètre 1 : window : fenptre du jeu
    La fonction timer3s(window) est utilisée pour afficher un compte à rebours de 3 secondes à l'écran.
    """
    # Vérifie l'état du compte à rebours en fonction du timer
    if Models.ball['timer'] >= 2 * (Models.INITIAL_TIMER / 3):
        # Affiche le texte "3" à l'écran
        displayOnScreen(window, "3", 590, 160, (255, 255, 255), 200)
    elif Models.ball['timer'] >= (Models.INITIAL_TIMER / 3):
        # Affiche le texte "2" à l'écran
        displayOnScreen(window, "2", 590, 160, (255, 255, 255), 200)
    else:
        # Affiche le texte "1" à l'écran
        displayOnScreen(window, "1", 590, 160, (255, 255, 255), 200)

    # Décrémente le timer de 1 à chaque appel de la fonction
    Models.ball['timer'] -= 1


def drawPlayerRect(window, color, rect):
    """
    Paramètre 1 : window : la fenêtre sur laquelle dessiner le rectangle.
    Paramètre 1 : color : la couleur du rectangle.
    Paramètre 1 : rect : rectangle à dessiner.
    La fonction pygame.draw.rect() est utilisée pour dessiner le rectangle sur la fenêtre.
    """
    # Dessine un rectangle sur la fenêtre avec la couleur spécifiée et les coordonnées du rectangle
    pygame.draw.rect(window, color, rect)


def drawDictOfPlayerRect(window, dictOfPlayerRect):
    """
    Paramètre 1 : window : la fenêtre sur laquelle dessiner le rectangle.
    Paramètre 1 : dictOfPlayerRect : dictionnaire des rectangles des plateformes.
    La fonction itère sur chaque clé (couleur) du dictionnaire dictOfPlayerRect, qui contient les rectangles des joueurs.
    Pour chaque couleur, la fonction appelle drawPlayerRect(window, color, rect) pour dessiner le rectangle du joueur
    correspondant.
    """
    # Parcourt chaque couleur dans le dictionnaire de rectangles des joueurs
    for color in dictOfPlayerRect.keys():
        # Dessine le rectangle du joueur correspondant à la couleur spécifiée
        drawPlayerRect(window, color, dictOfPlayerRect[color])


def returnRectOfPlayer(x, y):
    """
    Paramètre 1 : x : position 'x' voulu.
    Paramètre 1 : y : position 'y' voulu.
    La fonction crée un nouvel objet pygame.Rect en utilisant les coordonnées x et y spécifiées,
    ainsi que la largeur et la hauteur du joueur provenant du modèle Models.
    """
    # Crée et retourne un objet pygame.Rect représentant le rectangle du joueur
    return pygame.Rect(x, y, Models.player1["width"], Models.player1["height"])


def returnRectOfBall(x, y):
    """
    Paramètre 1 : x : position 'x' voulu.
    Paramètre 1 : y : position 'x' voulu.
    La fonction crée un nouvel objet pygame.Rect en utilisant les coordonnées x et y spécifiées,
    ainsi que le rayon de la balle provenant du modèle Models.
    """
    # Crée et retourne un objet pygame.Rect représentant le rectangle de la balle
    # Le rectangle est centré sur les coordonnées (x, y) spécifiées et a une largeur
    # et une hauteur égale au double du rayon de la balle
    return pygame.Rect(x - Models.ball['radius'], y - Models.ball['radius'],
                       2 * Models.ball['radius'], 2 * Models.ball['radius'])


def drawBallRect(window, color, rect):
    """
    Paramètre 1 : window : la fenêtre sur laquelle dessiner la balle.
    Paramètre 1 : color : couleur de la balle
    Paramètre 1 : rect : rectangle de la balle
    La fonction utilise la bibliothèque Pygame pour dessiner un cercle représentant la balle sur la fenêtre spécifiée.
    """
    # Dessine un cercle représentant la balle sur la fenêtre donnée
    pygame.draw.circle(window, color, (rect.left + Models.ball['radius'], rect.top + Models.ball['radius']),
                       Models.INITIAL_RADIUS)


def drawDictOfBallRect(window, dictOfBallRect):
    """
    Paramètre 1 : window : la fenêtre sur laquelle dessiner la balle.
    Paramètre 1 : dictOfBallRect : Dictionnaire contenant les rectangles des balles.
    Dessine les rectangles de balle correspondant à chaque couleur dans le dictionnaire sur la fenêtre donnée
    Le dictionnaire contient des paires clé-valeur où la clé est la couleur de la balle et la valeur est le rectangle
    correspondant
    """
    # Parcourt les clés (couleurs) du dictionnaire
    for color in dictOfBallRect.keys():
        # Dessine le rectangle de balle correspondant à la couleur sur la fenêtre
        drawBallRect(window, color, dictOfBallRect[color])
