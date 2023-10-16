import pygame
from ship import*
from ennemis import *

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
