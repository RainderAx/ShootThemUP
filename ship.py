# Chargement des images
vaisseau_img = pygame.image.load("piou.jpg")
tir_img = pygame.image.load("sphere.png")

# Redimensionnement des images
vaisseau_img = pygame.transform.scale(vaisseau_img, (64, 64))
tir_img = pygame.transform.scale(tir_img, (32, 32))

# Position initiale du vaisseau
vaisseau_x = largeur // 2 - 32
vaisseau_y = hauteur - 100

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
    
    # Déplacement du vaisseau avec les touches directionnelles
    touches = pygame.key.get_pressed()
    if touches[pygame.K_LEFT] and vaisseau_x > 0:
        vaisseau_x -= 5
    if touches[pygame.K_RIGHT] and vaisseau_x < largeur - 64:
        vaisseau_x += 5

    # Mise à jour des tirs
    for tir in tirs:
        tir["y"] -= tir["vit"]

        # Suppression des tirs qui sont sortis de l'écran
        if tir["y"] < 0:
            tirs.remove(tir)