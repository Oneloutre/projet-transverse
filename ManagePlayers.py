import pygame
import Models


def move(player):
    keys = pygame.key.get_pressed()
    if 0-Models.INITIAL_PLAYER_SPEED <= player["x"] <= ((Models.BOX_WIDTH//2)-player["width"])+Models.INITIAL_PLAYER_SPEED:
        if keys[pygame.K_q] and player["x"] > 0:
            player["x"] -= Models.INITIAL_PLAYER_SPEED
        if keys[pygame.K_d] and player["x"] < ((Models.BOX_WIDTH//2)-player["width"]):
            player["x"] += Models.INITIAL_PLAYER_SPEED
    elif (Models.BOX_WIDTH//2)+15-Models.INITIAL_PLAYER_SPEED <= player["x"] <= Models.BOX_WIDTH-Models.player2["width"]+Models.INITIAL_PLAYER_SPEED:
        if keys[pygame.K_LEFT] and player["x"] > (Models.BOX_WIDTH//2)+15:
            player["x"] -= Models.INITIAL_PLAYER_SPEED
        if keys[pygame.K_RIGHT] and player["x"] < Models.BOX_WIDTH-Models.player2["width"]:
            player["x"] += Models.INITIAL_PLAYER_SPEED
