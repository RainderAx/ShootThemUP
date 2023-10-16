import pygame
import random

# Charger l'image de l'ennemi et la redimensionner
ennemi_img = pygame.image.load("vex.jpg")
ennemi_img = pygame.transform.scale(ennemi_img, (64, 64))

import pygame
import random

# Charger l'image de l'ennemi et la redimensionner
ennemi_img = pygame.image.load("vex.jpg")
ennemi_img = pygame.transform.scale(ennemi_img, (64, 64))

class Ennemi:
    def __init__(self):
        self.x = random.randint(0, largeur - 64)
        self.y = -64
        self.vit = random.randint(1, 3) + (score // 100)

    def deplacer(self):
        self.y += self.vit

    def verifier_collision_tirs(self, tirs):
        for tir in tirs:
            if (
                self.x < tir.x < self.x + 64
                and self.y < tir.y < self.y + 64
            ):
                return True
        return False

    def verifier_collision_vaisseau(self, vaisseau_x, vaisseau_y):
        if (
            vaisseau_x + 64 > self.x
            and vaisseau_x < self.x + 64
            and vaisseau_y + 64 > self.y
            and vaisseau_y < self.y + 64
        ):
            return True
        return False

class Sbire(Ennemi):
    def __init__(self):
        super().__init__()
        self.vit = random.randint(4, 6) + (score // 100)
        self.image = pygame.image.load("sbire.webp")
        self.image = pygame.transform.scale(self.image, (48, 48))

# Créer un sbire
sbire = Sbire()

# Créer un ennemi
ennemi = Ennemi()

# Liste des ennemis
ennemis = []
ennemis.append(sbire,ennemi)

# Création d'un ennemi
def creer_ennemi():
    ennemis = {
        "x": random.randint(0, largeur - 64),
        "y": -64,
    }
    ennemis.append(ennemi,sbire)

def mise_a_jour_ennemis(tirs, vaisseau_x, vaisseau_y, hauteur, score):
    for ennemi in ennemis:
        # Déplacer l'ennemi
        ennemi.deplacer()

        # Créer un ennemi à intervalles réguliers
        if score > 900 and random.randint(0, 100) < 2:
            creer_ennemi()

        # Vérification des collisions entre les ennemis et les tirs
        ennemi_touche = False
        for tir in tirs:
            if (
                tir.x > ennemi.x
                and tir.x < ennemi.x + 64
                and tir.y > ennemi.y
                and tir.y < ennemi.y + 64
            ):
                ennemi_touche = True
                tirs.remove(tir)
                score += 10
                break  # Sortir de la boucle si un tir touche un ennemi

        if ennemi_touche:
            ennemis.remove(ennemi)

        # Vérification des collisions entre les ennemis et le vaisseau
        if (
            vaisseau_x + 64 > ennemi.x
            and vaisseau_x < ennemi.x + 64
            and vaisseau_y + 64 > ennemi.y
            and vaisseau_y < ennemi.y + 64
        ):
            running = False

        # Suppression des ennemis qui sont sortis de l'écran
        if ennemi.y > hauteur:
            ennemis.remove(ennemi)