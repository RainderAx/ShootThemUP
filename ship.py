import pygame



# Chargement des images
vaisseau_img = pygame.image.load("piou.jpg")


# Redimensionnement des images
vaisseau_img = pygame.transform.scale(vaisseau_img, (64, 64))

class Vaisseau:
    def __init__(self, largeur, hauteur):
        self.image = vaisseau_img
        self.x = largeur // 2 - 32
        self.y = hauteur - 100

    def deplacer(self, largeur, touches):
        if touches[pygame.K_LEFT] and self.x > 0:
            self.x -= 5
        if touches[pygame.K_RIGHT] and self.x < largeur - 64:
            self.x += 5

