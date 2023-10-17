import asyncio

class Tir:
    def __init__(self, x, y, vit, img):
        self.x = x
        self.y = y
        self.vit = vit
        self.img = img

    def deplacer(self):
        self.y -= self.vit

    def afficher(self, fenetre):
        fenetre.blit(self.img, (self.x, self.y))

    async def tirer(self, x, y, tirs, tir_vitesse, tir_img):
        tir = Tir(x, y, tir_vitesse, tir_img)
        tirs.append(tir)
        await asyncio.sleep(0.5)

