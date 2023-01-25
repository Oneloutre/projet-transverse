import ballon
from joueur import Joueur


class Game:
    def __init__(self):
        self.joueur = Joueur()
        self.keyPressed = {}
