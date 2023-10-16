from ship import Vaisseau 
import pygame


tir_img = pygame.image.load("sphere.png")
tir_img = pygame.transform.scale(tir_img, (32, 32))


class Tir:
    def __init__(self, x, y):
        self.image = tir_img
        self.x = x
        self.y = y
        self.vitesse = 5

    def deplacer(self):
        self.y -= self.vitesse

class Jeu:
    def __init__(self, largeur, hauteur):
        self.vaisseau = Vaisseau(largeur, hauteur)
        self.tirs = []

    def tirer(self):
        tir = Tir(self.vaisseau.x, self.vaisseau.y)
        self.tirs.append(tir)

    def mise_a_jour_tirs(self):
        tirs_a_supprimer = []
        for tir in self.tirs:
            tir.deplacer()
            if tir.y < 0:
                tirs_a_supprimer.append(tir)

        for tir in tirs_a_supprimer:
            self.tirs.remove(tir)