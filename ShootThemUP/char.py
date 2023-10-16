import random 
import pygame

# Chargement des images
vaisseau_img = pygame.image.load("piou.jpg")
ennemi_img = pygame.image.load("vex.jpg")
tir_img = pygame.image.load("sphere.png")

# Redimensionnement des images
vaisseau_img = pygame.transform.scale(vaisseau_img, (64, 64))
ennemi_img = pygame.transform.scale(ennemi_img, (64, 64))
tir_img = pygame.transform.scale(tir_img, (32, 32))

# Position initiale du vaisseau
vaisseau_x = largeur // 2 - 32
vaisseau_y = hauteur - 100

# Liste des ennemis
ennemis = []

# Création d'un ennemi
def creer_ennemi():
    ennemi = {
        "x": random.randint(0, largeur - 64),
        "y": -64,
        "vit": random.randint(1, 3)
    }
    ennemis.append(ennemi)

# Gestion des tirs
tirs = []
tir_vitesse = 5

def tirer(x, y):
    tir = {
        "x": x,
        "y": y,
        "vit": tir_vitesse
    }
    tirs.append(tir)

score = 0