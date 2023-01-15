class Voiture:
    nb_voiture = 0
    def __init__(self, couleur):
        Voiture.nb_voiture += 1
        self.couleur = couleur
    def avancer(self):
        print("La voiture", self.couleur, "avance vite")

voiture1 = Voiture('Rouge')
voiture1.avancer()
voiture2 = Voiture('Jaune')
voiture2.avancer()
voiture3 = Voiture("Vert")
voiture3.avancer()