import pygame
import random
from map import Map
from vaisseau import Vaisseau
from ennemi import Ennemi
from tir import Tir


# Initialisation de Pygame
pygame.init()

# Dimensions de la fenêtre de jeu
largeur = 800
hauteur = 600

# Couleurs
BLANC = (255, 255, 255)
NOIR = (0, 0, 0)


# Création de la fenêtre de jeu
fenetre = pygame.display.set_mode((largeur, hauteur))
pygame.display.set_caption("Shoot Them Up")

# Chargement des images
vaisseau_img = pygame.image.load("piou.jpg")
ennemi_img = pygame.image.load("vex.jpg")
tir_img = pygame.image.load("sphere.jpg")
sbire_img = pygame.image.load("sbire.jpg")

# Redimensionnement des images
vaisseau_img = pygame.transform.scale(vaisseau_img, (50, 50))
ennemi_img = pygame.transform.scale(ennemi_img, (64, 64))
tir_img = pygame.transform.scale(tir_img, (32, 32))
sbire_img = pygame.transform.scale(sbire_img, (48, 48))


# Position initiale du vaisseau
vaisseau = Vaisseau(largeur // 2 - 32, hauteur - 100, vaisseau_img)

# Liste des ennemis
ennemis = []

# Gestion des tirs
tirs = []
tir_vitesse = 5

score = 0

# Création de la carte
carte = Map(largeur, hauteur, NOIR)

# Boucle principale du jeu
running = True
clock = pygame.time.Clock()

while running:
    # Gestion des événements
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                Tir.tirer(vaisseau.x + 16, vaisseau.y, tirs, tir_vitesse, tir_img)
                

    # Déplacement du vaisseau avec les touches directionnelles
    touches = pygame.key.get_pressed()
    vaisseau.deplacer(touches, largeur)

    # Mise à jour des ennemis
    for ennemi in ennemis:
        ennemi.deplacer()

        # Vérification des collisions entre les ennemis et les tirs
        for tir in tirs:
            if ennemi.collision(tir):
                ennemis.remove(ennemi)
                tirs.remove(tir)
                score +=10

        # Vérification des collisions entre les ennemis et le vaisseau
        if vaisseau.collision(ennemi):
            running = False

        # Suppression des ennemis qui sont sortis de l'écran
        if ennemi.y > hauteur:
            ennemis.remove(ennemi)

    # Mise à jour des tirs
    for tir in tirs:
        tir.deplacer()

        # Suppression des tirs qui sont sortis de l'écran
        if tir.y < 0:
            tirs.remove(tir)

    # Création d'un ennemi à intervalles réguliers
    if random.randint(0, 100) < 1+(score/500):
        vitesse = random.randint(2 , 3) + (score/200)
        if vitesse > 7 :
            vitesse = 7
        ennemi = Ennemi(random.randint(0, largeur - 64), -64, ennemi_img, vitesse)
        ennemis.append(ennemi)
        if random.randint(0, 2) >=2: 
            ennemi = Ennemi(random.randint(0, largeur - 64), -64, sbire_img, vitesse + 1)
            ennemis.append(ennemi)
            
            
    # Difficulté en fonction du score
    if score > 900:
        if random.randint(0, 100) < 2:
            ennemi = Ennemi(random.randint(0, largeur - 64), -64, ennemi_img, vitesse)
            ennemis.append(ennemi)

    # Dessin des éléments du jeu
    carte.dessiner(fenetre)
    vaisseau.afficher(fenetre)
    for ennemi in ennemis:
        ennemi.afficher(fenetre)
    for tir in tirs:
        tir.afficher(fenetre)

    #affichage du score 
    font = pygame.font.Font(None, 36)
    texte_score = font.render("Score:" + str(score), True, BLANC)
    fenetre.blit(texte_score,(10,10))

    # Rafraîchissement de l'écran
    pygame.display.flip()

    # Limitation de la vitesse de rafraîchissement
    clock.tick(60)

# Fermeture de Pygame
pygame.quit()  