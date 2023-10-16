class Map:
    def __init__(self, largeur, hauteur, couleur):
        self.largeur = largeur
        self.hauteur = hauteur
        self.couleur = couleur

    def dessiner(self, fenetre):
        fenetre.fill(self.couleur)