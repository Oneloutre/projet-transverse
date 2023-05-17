import math

player1 = {"points": 0, "x": 200, "y": 500, "width": 100, "height": 10}
player2 = {"points": 0, "x": 1000, "y": 500, "width": 100, "height": 10}
INITIAL_PLAYER_SPEED = 2

SCORE_MAX = 10

""" The gravity, g."""
GRAVITY = 9.80665
""" The time interval, Δt."""
INTERVAL = 0.04
""" The friction on left an right, frictionX."""
FRICTION_X = 1
""" The friction on ground, frictionY."""
FRICTION_Y = 1
""" The box width in which the ball bounces."""
BOX_WIDTH = 1280
""" The box height in which the ball bounces."""
BOX_HEIGHT = 720

""" The initial position x(0) of the ball."""
INITIAL_X = 50
""" The initial position y(0) of the ball."""
INITIAL_Y = 450
""" The initial speed V(0) of the ball."""
INITIAL_SPEED = 105
""" The initial angle α of the ball."""
INITIAL_ANGLE = 60
""" The radius of the ball."""
INITIAL_RADIUS = 30

INITIAL_TIMER = 900

QUIT = False

MENU = True

""" The ball at time 0."""
ball = {'x': INITIAL_X,
        'y': INITIAL_Y,
        'speedX': INITIAL_SPEED * math.cos(math.radians(INITIAL_ANGLE)),
        'speedY': INITIAL_SPEED * math.sin(math.radians(INITIAL_ANGLE)),
        'angle': INITIAL_ANGLE,
        'radius': INITIAL_RADIUS,
        'visible': True,
        'timer': INITIAL_TIMER}
