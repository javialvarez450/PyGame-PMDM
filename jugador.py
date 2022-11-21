import pygame

from laser import Laser

class Jugador(pygame.sprite.Sprite):

    def __init__(self, pos,restriccion,velocidad):
        super().__init__()
        self.image = pygame.image.load('resources/443-4431365_spaceship-sprite-png-transparent-png.png')

        self.rotacion= 0
        self.rect = self.image.get_rect(midbottom=pos)
        self.velocidad = velocidad
        self.max_x_restriccion=restriccion
        self.prep=True
        self.tiempo_laser = 0
        self.cooldown_laser = 600

        self.lasers = pygame.sprite.Group()

    def activa_teclas(self):
        teclas = pygame.key.get_pressed()

        if teclas[pygame.K_RIGHT]:
            self.rect.x += self.velocidad
        elif teclas[pygame.K_LEFT]:
            self.rect.x -=  self.velocidad

        if teclas[pygame.K_SPACE]:
            self.disparos_laser()
            self.prep=False
            self.tiempo_laser=pygame.time.get_ticks()

    def recarga(self):
        if not self.prep:
            tiempo_actual = pygame.time.get_ticks()
            if tiempo_actual - self.tiempo_laser >= self.cooldown_laser:
                self.prep=True

    def disparos_laser(self):
        self.lasers.add(Laser(self.rect.center,-8,self.rect.bottom))

    def restriccion(self):
        if self.rect.left <= 0:
            self.rect.left=0
        if self.rect.right >= self.max_x_restriccion:
            self.rect.right =self.max_x_restriccion

    def update(self):
        self.activa_teclas()
        self.restriccion()
        self.recarga()
        self.lasers.update()