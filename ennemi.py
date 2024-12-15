import pygame
import random

class Ennemi:
    def __init__(self, x, y, img, vit):
        self.x = x
        self.y = y
        self.img = img
        self.vit = vit

    def deplacer(self):
        self.y += self.vit

    def collision(self, tir):
        if (
            tir.x > self.x
            and tir.x < self.x + 64
            and tir.y > self.y
            and tir.y < self.y + 64
        ):
            return True
        else:
            return False

    def afficher(self, fenetre):
        fenetre.blit(self.img, (self.x, self.y))