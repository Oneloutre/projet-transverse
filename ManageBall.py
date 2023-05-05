import math

import pygame.rect

import Models


def moveBall():
    bounceX = False
    Models.ball['x'] += Models.ball['speedX'] * math.cos(
        math.radians(Models.ball['angle'])) * Models.INTERVAL
    Models.ball['y'] -= Models.INTERVAL * (
                Models.ball['speedY'] - (Models.GRAVITY * Models.INTERVAL))
    Models.ball['speedY'] += - Models.GRAVITY * Models.INTERVAL
    ball_rect = pygame.Rect(Models.ball['x'] - Models.ball['radius'], Models.ball['y'] - Models.ball['radius'],
                            2 * Models.ball['radius'], 2 * Models.ball['radius'])
    collisionsWithP1(ball_rect)
    collisionWithFilet(ball_rect)
    rectPlayer = pygame.Rect(Models.player2["x"], Models.player2["y"]+50, 125, 290)
    if ball_rect.colliderect(rectPlayer):
        if Models.player2["jumping"]:
            Models.ball['speedY'] = - Models.ball['speedY'] * Models.FRICTION_Y + Models.STRONG
        else:
            Models.ball['speedY'] = - Models.ball['speedY'] * Models.FRICTION_Y
        Models.ball['speedX'] = Models.ball['speedX'] * Models.FRICTION_X + Models.STRONG
        Models.ball['angle'] = 105
    if Models.ball['x'] - Models.ball['radius'] <= 0:
        Models.ball['x'] = 0 + Models.ball['radius']
        bounceX = True
    if Models.ball['x'] + Models.ball['radius'] >= Models.BOX_WIDTH:
        Models.ball['x'] = Models.BOX_WIDTH - Models.ball['radius']
        bounceX = True
    if Models.ball['y'] - Models.ball['radius'] >= Models.BOX_HEIGHT:
        Models.ball['y'] = Models.BOX_HEIGHT + Models.ball['radius']
        Models.ball['speedY'] = - Models.ball['speedY'] * Models.FRICTION_Y
        Models.ball['speedX'] = Models.ball['speedX'] * Models.FRICTION_X
    if bounceX:
        Models.ball['angle'] = (180 - Models.ball['angle']) % 360
        Models.ball['speedX'] = Models.ball['speedX'] * Models.FRICTION_X


def collisionWithFilet(ball_rect):
    if ball_rect.colliderect(Models.FiletRect):
        if Models.ball['x'] - Models.ball['radius'] <= Models.FiletRect.left:
            print("point player2")
        if Models.ball['x'] + Models.ball['radius'] >= Models.FiletRect.right:
            print("point player1")
            Models.ball['speedX'] = 0
        Models.ball["visible"] = False


def collisionsWithP1(ball_rect):
    rectPlayer = pygame.Rect(Models.player1["x"] + 100, Models.player1["y"] + 50, 125, 290)
    if ball_rect.colliderect(rectPlayer):
        if Models.player1["jumping"]:
            Models.ball['speedY'] = - Models.ball['speedY'] * Models.FRICTION_Y + Models.STRONG
        else:
            Models.ball['speedY'] = - Models.ball['speedY'] * Models.FRICTION_Y
        Models.ball['speedX'] = Models.ball['speedX'] * Models.FRICTION_X + Models.STRONG
        Models.ball['angle'] = 75
