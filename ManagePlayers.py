import pygame
import Models


def move(player, playersParameters):
    keys = pygame.key.get_pressed()
    if 0-playersParameters["speed"] <= player["x"] <= ((Models.BOX_WIDTH//2)-player["width"])+playersParameters["speed"]:
        if keys[pygame.K_q] and player["x"] > 0:
            player["x"] -= playersParameters["speed"]
        if keys[pygame.K_d] and player["x"] < ((Models.BOX_WIDTH//2)-player["width"]):
            player["x"] += playersParameters["speed"]
    elif (Models.BOX_WIDTH//2)+15-playersParameters["speed"] <= player["x"] <= Models.BOX_WIDTH-Models.player2["width"]+playersParameters["speed"]:
        if keys[pygame.K_LEFT] and player["x"] > (Models.BOX_WIDTH//2)+15:
            player["x"] -= playersParameters["speed"]
        if keys[pygame.K_RIGHT] and player["x"] < Models.BOX_WIDTH-Models.player2["width"]:
            player["x"] += playersParameters["speed"]
