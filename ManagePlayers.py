import pygame


def jump(player, playersParameters):
    if player["jumping"] and player["y"] > 300 - playersParameters["jumpHeight"]:
        player["y"] -= playersParameters["jumpSpeed"]
    elif player["y"] < 300:
        player["jumping"] = False
        player["y"] += playersParameters["jumpSpeed"]


def move(player, playersParameters):
    keys = pygame.key.get_pressed()
    if -41 < player["x"] < 401:
        if keys[pygame.K_q] and player["x"] > -40:
            player["x"] -= playersParameters["speed"]
        if keys[pygame.K_d] and player["x"] < 400:
            player["x"] += playersParameters["speed"]
        if keys[pygame.K_z] and player["y"] == 300:
            player["jumping"] = True
    elif 649 < player["x"] < 1176:
        if keys[pygame.K_LEFT] and player["x"] > 650:
            player["x"] -= playersParameters["speed"]
        if keys[pygame.K_RIGHT] and player["x"] < 1175:
            player["x"] += playersParameters["speed"]
        if keys[pygame.K_UP] and player["y"] == 300:
            player["jumping"] = True
