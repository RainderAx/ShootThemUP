import pygame

class Vaisseau:
    def __init__(self, x, y, img):
        self.x = x
        self.y = y
        self.img = img

    def deplacer(self, touches, largeur):
        if touches[pygame.K_LEFT] and self.x > 0:
            self.x -= 5
        if touches[pygame.K_RIGHT] and self.x < largeur - 64:
            self.x += 5

    def collision(self, ennemi):
        if (
            self.x + 64 > ennemi.x
            and self.x < ennemi.x + 64
            and self.y + 64 > ennemi.y
            and self.y < ennemi.y + 64
        ):
            return True
        else:
            return False

    def afficher(self, fenetre):
        fenetre.blit(self.img, (self.x, self.y))
