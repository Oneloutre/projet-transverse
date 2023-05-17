import pygame
import Models
import math


def moveBall():
    Models.ball['x'] += Models.ball['speedX'] * math.cos(
        math.radians(Models.ball['angle'])) * Models.INTERVAL
    Models.ball['y'] -= Models.INTERVAL * (
            Models.ball['speedY'] - (Models.GRAVITY * Models.INTERVAL))
    Models.ball['speedY'] += - Models.GRAVITY * Models.INTERVAL
    ball_rect = pygame.Rect(Models.ball['x'] - Models.ball['radius'], Models.ball['y'] - Models.ball['radius'],
                            2 * Models.ball['radius'], 2 * Models.ball['radius'])
    collisionFilet(ball_rect)

    player1Rect = pygame.Rect(Models.player1["x"], Models.player1["y"], Models.player1["width"],
                              Models.player1["height"])
    collisionPlayers(ball_rect, player1Rect)

    player2Rect = pygame.Rect(Models.player2["x"], Models.player2["y"], Models.player2["width"],
                              Models.player2["height"])
    collisionPlayers(ball_rect, player2Rect)

    collisionLimits(ball_rect)
    collisionGround(ball_rect)


def bouceX():
    Models.ball['angle'] = (180 - Models.ball['angle']) % 360
    Models.ball['speedX'] = Models.ball['speedX'] * Models.FRICTION_X


def collisionFilet(ball_rect):
    FiletRect = pygame.Rect((Models.BOX_WIDTH // 2) + 3, Models.BOX_HEIGHT - 378, 14, 380)
    if ball_rect.colliderect(FiletRect):
        if FiletRect.top - 4 <= ball_rect.bottom <= FiletRect.top + 4:
            Models.ball['speedY'] = - Models.ball['speedY'] * Models.FRICTION_Y
            Models.ball['speedX'] = Models.ball['speedX'] * Models.FRICTION_X
        elif ball_rect.right == FiletRect.right:
            bouceX()
        elif ball_rect.left == FiletRect.left:
            bouceX()


def collisionPlayers(ball_rect, playerRect):
    if ball_rect.colliderect(playerRect):
        if playerRect.left - 4 <= ball_rect.right <= playerRect.left + 4:
            Models.ball["x"] = playerRect.left - Models.ball["radius"] - 4
            bouceX()
        if playerRect.right - 4 <= ball_rect.left <= playerRect.right + 4:
            Models.ball["x"] = playerRect.right + Models.ball["radius"] + 4
            bouceX()
        else:
            Models.ball['speedY'] = - Models.ball['speedY'] * Models.FRICTION_Y
            Models.ball['speedX'] = Models.ball['speedX'] * Models.FRICTION_X


def collisionGround(ball_rect):
    if ball_rect.bottom >= Models.BOX_HEIGHT:
        if Models.ball["x"] < (Models.BOX_WIDTH // 2):
            Models.player2["points"] += 1
            placeBall(Models.BOX_WIDTH - (Models.INITIAL_RADIUS + 10), Models.INITIAL_Y, 120)
        elif (Models.BOX_WIDTH // 2) < Models.ball["x"]:
            Models.player1["points"] += 1
            placeBall(Models.INITIAL_RADIUS + 10, Models.INITIAL_Y, 60)


def collisionLimits(ball_rect):
    if ball_rect.left == 0:
        bouceX()
    if ball_rect.right == Models.BOX_WIDTH:
        bouceX()


def placeBall(x, y, angle):
    Models.ball = {'x': x,
                   'y': y,
                   'speedX': Models.INITIAL_SPEED * math.cos(math.radians(angle)),
                   'speedY': Models.INITIAL_SPEED * math.sin(math.radians(angle)),
                   'angle': angle,
                   'radius': Models.INITIAL_RADIUS,
                   'visible': True,
                   'timer': Models.INITIAL_TIMER,
                   'color': Models.INITIAL_BALL_COLOR}
