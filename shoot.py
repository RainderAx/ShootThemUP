import pygame
import random
import time

# Initialisation de Pygame
pygame.init()

# Dimensions de la fenêtre de jeu
largeur = 800
hauteur = 600

# Couleurs
BLANC = (255, 255, 255)
NOIR = (0, 0, 0)
ROUGE = (255, 0, 0)

# Création de la fenêtre de jeu
fenetre = pygame.display.set_mode((largeur, hauteur))
pygame.display.set_caption("Shoot Them Up")

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
                tirer(vaisseau_x + 16, vaisseau_y)

    # Déplacement du vaisseau avec les touches directionnelles
    touches = pygame.key.get_pressed()
    if touches[pygame.K_LEFT] and vaisseau_x > 0:
        vaisseau_x -= 5
    if touches[pygame.K_RIGHT] and vaisseau_x < largeur - 64:
        vaisseau_x += 5

    # Mise à jour des ennemis
    for ennemi in ennemis:
        ennemi["y"] += ennemi["vit"]

        # Vérification des collisions entre les ennemis et les tirs
        for tir in tirs:
            if (
                tir["x"] > ennemi["x"]
                and tir["x"] < ennemi["x"] + 64
                and tir["y"] > ennemi["y"]
                and tir["y"] < ennemi["y"] + 64
            ):
                ennemis.remove(ennemi)
                tirs.remove(tir)
                score +=10

        # Vérification des collisions entre les ennemis et le vaisseau
        if (
            vaisseau_x + 64 > ennemi["x"]
            and vaisseau_x < ennemi["x"] + 64
            and vaisseau_y + 64 > ennemi["y"]
            and vaisseau_y < ennemi["y"] + 64
        ):
            running = False

        # Suppression des ennemis qui sont sortis de l'écran
        if ennemi["y"] > hauteur:
            ennemis.remove(ennemi)

    # Mise à jour des tirs
    for tir in tirs:
        tir["y"] -= tir["vit"]

        # Suppression des tirs qui sont sortis de l'écran
        if tir["y"] < 0:
            tirs.remove(tir)

    # Création d'un ennemi à intervalles réguliers
    if random.randint(0, 100) < 2:
        creer_ennemi()

    # Difficulté en fonction du score
    for ennemi in ennemis:
        Diff = (score + 200)/100
        Diff2= Diff + 1
        ennemi["vit"] = random.randint(int(Diff), int(Diff2))
    if Diff > 900:
        if random.randint(0, 100) < 2:
            creer_ennemi()
            
    # Dessin des éléments du jeu
    fenetre.fill(NOIR)
    fenetre.blit(vaisseau_img, (vaisseau_x, vaisseau_y))
    for ennemi in ennemis:
        fenetre.blit(ennemi_img, (ennemi["x"], ennemi["y"]))
    for tir in tirs:
        fenetre.blit(tir_img, (tir["x"], tir["y"]))

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
