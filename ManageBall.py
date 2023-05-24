import pygame
import Models
import math


def moveBall():
    """
    La fonction moveBall() gère le déplacement de la balle dans le jeu.
    """
    # Crée un rectangle représentant la position et la taille de la balle
    ball_rect = pygame.Rect(Models.ball['x'] - Models.ball['radius'], Models.ball['y'] - Models.ball['radius'],
                            2 * Models.ball['radius'], 2 * Models.ball['radius'])

    # Vérifie les collisions avec le filet
    collisionFilet(ball_rect)

    # Crée un rectangle représentant la position et la taille du joueur 1
    player1Rect = pygame.Rect(Models.player1["x"], Models.player1["y"], Models.player1["width"],
                              Models.player1["height"])
    # Vérifie les collisions avec le joueur 1
    collisionPlayers(ball_rect, player1Rect, Models.player1)

    # Crée un rectangle représentant la position et la taille du joueur 2
    player2Rect = pygame.Rect(Models.player2["x"], Models.player2["y"], Models.player2["width"],
                              Models.player2["height"])
    # Vérifie les collisions avec le joueur 2
    collisionPlayers(ball_rect, player2Rect, Models.player2)

    # Vérifie les collisions avec les limites de l'écran
    collisionLimits(ball_rect)

    # Vérifie les collisions avec le sol
    collisionGround(ball_rect)

    # Met à jour la position de la balle en fonction de sa vitesse et de son angle
    Models.ball['x'] += Models.ball['speedX'] * math.cos(math.radians(Models.ball['angle'])) * Models.INTERVAL
    Models.ball['y'] -= Models.INTERVAL * (Models.ball['speedY'] - (Models.GRAVITY * Models.INTERVAL))

    # Met à jour la vitesse verticale de la balle en tenant compte de la gravité
    Models.ball['speedY'] += -Models.GRAVITY * Models.INTERVAL


def bouceX():
    """
    La fonction bouceX() est utilisée pour inverser la direction
    horizontale de la balle lorsqu'elle rebondit sur une surface.
    """
    # Inverse l'angle de la balle horizontalement
    Models.ball['angle'] = (180 - Models.ball['angle']) % 360


def collisionFilet(ball_rect):
    """
    Paramètre 1 : ball_rect: rectangle de la balle
    La fonction collisionFilet(ball_rect) est utilisée pour détecter
    et gérer les collisions entre la balle et le filet dans le jeu.
    """
    FiletRect = pygame.Rect((Models.BOX_WIDTH // 2) + 3, Models.BOX_HEIGHT - 378, 14, 380)
    if ball_rect.colliderect(FiletRect):
        if FiletRect.top - 4 <= ball_rect.bottom <= FiletRect.top + 4:
            # Rebond vertical de la balle
            Models.ball['speedY'] = -Models.ball['speedY']
        elif FiletRect.right - 4 <= ball_rect.right <= FiletRect.right + 4:
            # Décalage de la position de la balle vers la gauche et inversion de l'angle horizontal
            Models.ball["x"] -= 4
            bouceX()
        elif FiletRect.left - 4 <= ball_rect.left <= FiletRect.left + 4:
            # Décalage de la position de la balle vers la droite et inversion de l'angle horizontal
            Models.ball["x"] += 4
            bouceX()


def collisionPlayers(ball_rect, playerRect, player):
    """
    Paramètre 1 : ball_rect: rectangle de la balle
    Paramètre 2 : playerRect: rectangle du joueur
    Paramètre 3 : player: paramètre du joueur
    a fonction collisionPlayers(ball_rect, playerRect, player) est utilisée
    pour détecter et gérer les collisions entre la balle et les joueurs dans le jeu.
    """
    if ball_rect.colliderect(playerRect):
        if playerRect.left - 4 <= ball_rect.right <= playerRect.left + 4:
            # Décalage de la position de la balle vers la gauche et inversion de l'angle horizontal
            Models.ball["x"] = playerRect.left - Models.ball["radius"] - 4
            bouceX()
        if playerRect.right - 4 <= ball_rect.left <= playerRect.right + 4:
            # Décalage de la position de la balle vers la droite et inversion de l'angle horizontal
            Models.ball["x"] = playerRect.right + Models.ball["radius"] + 4
            bouceX()
        else:
            # Rebond vertical de la balle et ajustement de la vitesse horizontale en fonction du mouvement du joueur
            Models.ball['speedY'] = -Models.ball['speedY']
            if 90 < Models.ball['angle'] < 270:
                if player["move"] == 1:
                    Models.ball['speedX'] += 5
                elif player["move"] == -1:
                    Models.ball['speedX'] -= 5
            else:
                if player["move"] == 1:
                    Models.ball['speedX'] -= 5
                elif player["move"] == -1:
                    Models.ball['speedX'] += 5


def collisionGround(ball_rect):
    """
    Pramètre 1 : ball_rect: rectangle de la balle
    La fonction collisionGround(ball_rect) est utilisée pour détecter
    et gérer les collisions entre la balle et le sol dans le jeu.
    """
    if ball_rect.bottom >= Models.BOX_HEIGHT:
        if Models.ball["x"] < (Models.BOX_WIDTH // 2):
            # Incrémentation du score du joueur 2 et replacer la balle du côté droit
            Models.player2["points"] += 1
            placeBall(Models.BOX_WIDTH - (Models.INITIAL_RADIUS + 10), Models.INITIAL_Y, 120)
        elif (Models.BOX_WIDTH // 2) < Models.ball["x"]:
            # Incrémentation du score du joueur 1 et replacer la balle du côté gauche
            Models.player1["points"] += 1
            placeBall(Models.INITIAL_RADIUS + 10, Models.INITIAL_Y, 60)


def collisionLimits(ball_rect):
    """
    Paramètre 1 : ball_rect : rectangle de la balle
    La fonction collisionLimits(ball_rect) est utilisée pour détecter et
    gérer les collisions entre la balle et les limites horizontales de la boîte de jeu.
    """
    if -4 <= ball_rect.left <= 4:
        bouceX()
    if Models.BOX_WIDTH - 4 <= ball_rect.right <= Models.BOX_WIDTH + 4:
        bouceX()


def placeBall(x, y, angle):
    """
    Paramètre 1 : x : position 'x' voulu.
    Paramètre 2 : y : position 'y' voulu.
    Paramètre 3 : angle : 'angle' désiré.
    La fonction placeBall(x, y, angle) est utilisée pour placer
    la balle dans une position spécifiée avec une vitesse et un angle initiaux.
    """
    Models.ball = {'x': x,
                   'y': y,
                   'speedX': Models.INITIAL_SPEED * math.cos(math.radians(angle)),
                   'speedY': Models.INITIAL_SPEED * math.sin(math.radians(angle)),
                   'angle': angle,
                   'radius': Models.INITIAL_RADIUS,
                   'timer': Models.INITIAL_TIMER}
