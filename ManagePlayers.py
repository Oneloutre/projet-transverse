import pygame
import Models


def move(player):
    """
    Paramètre 1 : player: paramètre du joueur spécifié.
    La fonction move(player) gère le déplacement d'un joueur en fonction des touches de contrôle pressées.
    """
    keys = pygame.key.get_pressed()

    # Vérifie si le joueur se trouve dans la zone de déplacement du joueur 1 (à gauche de l'écran)
    if 0 - Models.INITIAL_PLAYER_SPEED <= player["x"] <= (
            (Models.BOX_WIDTH // 2) - player["width"]) + Models.INITIAL_PLAYER_SPEED:
        if keys[pygame.K_q] and player["x"] > 0:
            # Touche "q" pressée et le joueur ne dépasse pas le bord gauche de l'écran
            player["x"] -= Models.INITIAL_PLAYER_SPEED  # Déplacement du joueur vers la gauche
            player["move"] = 1  # Indique un mouvement vers la gauche
        elif keys[pygame.K_d] and player["x"] < ((Models.BOX_WIDTH // 2) - player["width"]):
            # Touche "d" pressée et le joueur ne dépasse pas le bord droit de l'écran
            player["x"] += Models.INITIAL_PLAYER_SPEED  # Déplacement du joueur vers la droite
            player["move"] = -1  # Indique un mouvement vers la droite
        else:
            player["move"] = 0  # Aucune touche de déplacement pressée, le joueur ne bouge pas

    # Vérifie si le joueur se trouve dans la zone de déplacement du joueur 2 (à droite de l'écran)
    elif (Models.BOX_WIDTH // 2) + 15 - Models.INITIAL_PLAYER_SPEED <= player["x"] <= Models.BOX_WIDTH - \
            Models.player2["width"] + Models.INITIAL_PLAYER_SPEED:
        if keys[pygame.K_LEFT] and player["x"] > (Models.BOX_WIDTH // 2) + 15:
            # Touche "flèche gauche" pressée et le joueur ne dépasse pas le bord gauche de l'écran
            player["x"] -= Models.INITIAL_PLAYER_SPEED  # Déplacement du joueur vers la gauche
            player["move"] = 1  # Indique un mouvement vers la gauche
        elif keys[pygame.K_RIGHT] and player["x"] < Models.BOX_WIDTH - Models.player2["width"]:
            # Touche "flèche droite" pressée et le joueur ne dépasse pas le bord droit de l'écran
            player["x"] += Models.INITIAL_PLAYER_SPEED  # Déplacement du joueur vers la droite
            player["move"] = -1  # Indique un mouvement vers la droite
        else:
            player["move"] = 0  # Aucune touche de déplacement pressée, le joueur ne bouge pas
