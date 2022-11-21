import pygame

class Marciano(pygame.sprite.Sprite):
    def __init__(self,x,y):
        super().__init__()
        self.image = pygame.image.load('resources/alien-monster_1f47e.png').convert_alpha()
        self.rect = self.image.get_rect(topleft =(x,y))

    def update(self,direccion):
        self.rect.x += direccion

class NaveEnemiga (pygame.sprite.Sprite):
    def __init__(self, lado,ancho_pantalla):
        super().__init__()
        self.image = pygame.image.load('resources/18-188897_spaceship-sprite-png-transparent-space-ship-sprite-png.png').convert_alpha()

        if lado == 'right':
            x = ancho_pantalla + 50
            self.velocidad = -3
        else:
            x = -50
            self.velocidad = 3
        self.rect = self.image.get_rect(topleft=(x, 80))
    def update(self):
        self.rect.x += self.velocidad
