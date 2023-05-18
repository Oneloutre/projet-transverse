import pygame
import Models
import math


def moveBall():
    ball_rect = pygame.Rect(Models.ball['x'] - Models.ball['radius'], Models.ball['y'] - Models.ball['radius'],
                            2 * Models.ball['radius'], 2 * Models.ball['radius'])
    collisionFilet(ball_rect)

    player1Rect = pygame.Rect(Models.player1["x"], Models.player1["y"], Models.player1["width"],
                              Models.player1["height"])
    collisionPlayers(ball_rect, player1Rect, Models.player1)

    player2Rect = pygame.Rect(Models.player2["x"], Models.player2["y"], Models.player2["width"],
                              Models.player2["height"])
    collisionPlayers(ball_rect, player2Rect, Models.player2)

    collisionLimits(ball_rect)
    collisionGround(ball_rect)
    Models.ball['x'] += Models.ball['speedX'] * math.cos(
        math.radians(Models.ball['angle'])) * Models.INTERVAL
    Models.ball['y'] -= Models.INTERVAL * (
            Models.ball['speedY'] - (Models.GRAVITY * Models.INTERVAL))
    Models.ball['speedY'] += - Models.GRAVITY * Models.INTERVAL


def bouceX():
    Models.ball['angle'] = (180 - Models.ball['angle']) % 360


def collisionFilet(ball_rect):
    FiletRect = pygame.Rect((Models.BOX_WIDTH // 2) + 3, Models.BOX_HEIGHT - 378, 14, 380)
    if ball_rect.colliderect(FiletRect):
        if FiletRect.top - 4 <= ball_rect.bottom <= FiletRect.top + 4:
            Models.ball['speedY'] = - Models.ball['speedY']
        elif FiletRect.right - 4 <= ball_rect.right <= FiletRect.right + 4:
            Models.ball["x"] = Models.ball["x"] - 4
            bouceX()
        elif FiletRect.left - 4 <= ball_rect.left <= FiletRect.left + 4:
            Models.ball["x"] = Models.ball["x"] + 4
            bouceX()


def collisionPlayers(ball_rect, playerRect, player):
    if ball_rect.colliderect(playerRect):
        if playerRect.left - 4 <= ball_rect.right <= playerRect.left + 4:
            Models.ball["x"] = playerRect.left - Models.ball["radius"] - 4
            bouceX()
        if playerRect.right - 4 <= ball_rect.left <= playerRect.right + 4:
            Models.ball["x"] = playerRect.right + Models.ball["radius"] + 4
            bouceX()
        else:
            Models.ball['speedY'] = - Models.ball['speedY']
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
    if ball_rect.bottom >= Models.BOX_HEIGHT:
        if Models.ball["x"] < (Models.BOX_WIDTH // 2):
            Models.player2["points"] += 1
            placeBall(Models.BOX_WIDTH - (Models.INITIAL_RADIUS + 10), Models.INITIAL_Y, 120)
        elif (Models.BOX_WIDTH // 2) < Models.ball["x"]:
            Models.player1["points"] += 1
            placeBall(Models.INITIAL_RADIUS + 10, Models.INITIAL_Y, 60)


def collisionLimits(ball_rect):
    if -4 <= ball_rect.left <= 4:
        bouceX()
    if Models.BOX_WIDTH - 4 <= ball_rect.right <= Models.BOX_WIDTH + 4:
        bouceX()


def placeBall(x, y, angle):
    Models.ball = {'x': x,
                   'y': y,
                   'speedX': Models.INITIAL_SPEED * math.cos(math.radians(angle)),
                   'speedY': Models.INITIAL_SPEED * math.sin(math.radians(angle)),
                   'angle': angle,
                   'radius': Models.INITIAL_RADIUS,
                   'timer': Models.INITIAL_TIMER}
