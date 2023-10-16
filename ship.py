import pygame

# Chargement des images
vaisseau_img = pygame.image.load("piou.jpg")
tir_img = pygame.image.load("sphere.png")

# Redimensionnement des images
vaisseau_img = pygame.transform.scale(vaisseau_img, (64, 64))
tir_img = pygame.transform.scale(tir_img, (32, 32))

class Vaisseau:
    def __init__(self, largeur, hauteur):
        self.image = vaisseau_img
        self.x = largeur // 2 - 32
        self.y = hauteur - 100

    def deplacer(self, touches):
        if touches[pygame.K_LEFT] and self.x > 0:
            self.x -= 5
        if touches[pygame.K_RIGHT] and self.x < largeur - 64:
            self.x += 5

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
