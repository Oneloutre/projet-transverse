import math
import pygame

player1 = {"x": 200, "y": 300, "jumping": False}
player2 = {"x": 1000, "y": 300, "jumping": False}
# , "rect": pygame.Rect(200, 300, 225, 290)

FiletRect = pygame.Rect(640, 300, 20, 390)

playersParameters = {"speed": 1, "jumpSpeed": 1, "jumpHeight": 200}

window_width = 1280
window_height = 720


STRONG = 10
""" The gravity, g."""
GRAVITY = 9.80665
""" The time interval, Δt."""
INTERVAL = 0.02
""" The friction on left an right, frictionX."""
FRICTION_X = 0.95
""" The friction on ground, frictionY."""
FRICTION_Y = 0.85
""" The box width in which the ball bounces."""
BOX_WIDTH = 1280
""" The box height in which the ball bounces."""
BOX_HEIGHT = 720

""" The initial position x(0) of the ball."""
INITIAL_X = 25
""" The initial position y(0) of the ball."""
INITIAL_Y = BOX_HEIGHT-25
""" The initial speed V(0) of the ball."""
INITIAL_SPEED = 140
""" The initial angle α of the ball."""
INITIAL_ANGLE = 75
""" The radius of the ball."""
INITIAL_RADIUS = 30

""" The ball at time 0."""
ball = {'x': INITIAL_X,
        'y': INITIAL_Y,
        'speedX': INITIAL_SPEED * math.cos(math.radians(INITIAL_ANGLE)),
        'speedY': INITIAL_SPEED * math.sin(math.radians(INITIAL_ANGLE)),
        'angle': INITIAL_ANGLE,
        'radius': INITIAL_RADIUS,
        'visible': True}