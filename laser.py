import pygame

class Laser (pygame.sprite.Sprite):
    def __init__(self,pos,velocidad ,altura_p):
        super().__init__()
        self.image = pygame.Surface((4,20))
        self.image.fill('white')
        self.rect = self.image.get_rect(center = pos)
        self.velocidad = velocidad
        self.altura_restriccion = altura_p

    def update(self):
        self.rect.y += self.velocidad
        self.destruir()

    def destruir (self):
        if self.rect.y <= -50 or self.rect.y >= self.altura_restriccion +50:
            self.kill()