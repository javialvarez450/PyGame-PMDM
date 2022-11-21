import sys
from random import choice, randint

import pygame

from jugador import Jugador
from marcianos import Marciano,NaveEnemiga
from laser import Laser


class Background(pygame.sprite.Sprite):
    def __init__(self, image_file, location):
        pygame.sprite.Sprite.__init__(self)  #call Sprite initializer
        self.image = pygame.image.load('resources/fUG2oM.jpg')
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location


class Juego:
    def __init__(self):
        jugador_sprite = Jugador((ancho_pantalla / 2, altura_pantalla),ancho_pantalla,7)
        self.jugador = pygame.sprite.GroupSingle(jugador_sprite)

        #Alien
        self.marcianos = pygame.sprite.Group()
        self.inicio_marcianos(filas=6,colum=8)
        self.direccion_marciano =3
        self.marciano_lasers= pygame.sprite.Group()

        #ExtraNave
        self.extraNave= pygame.sprite.GroupSingle()
        self.extraNave_spawn= randint(400,800)

    def inicio_marcianos(self,filas,colum,dist_x= 60,dist_y = 50,compensa_x= 350,compensa_y= 100):
        for fila_index, fila in enumerate(range(filas)):
            for col_index, col in enumerate(range(colum)):
                x = col_index * dist_x + compensa_x
                y = fila_index * dist_y + compensa_y

                marciano_sprite = Marciano(x,y)
                self.marcianos.add(marciano_sprite)
    def posicion_marcianos (self):
        total_marcianos = self.marcianos.sprites()
        for marciano in total_marcianos:
            if marciano.rect.right >= ancho_pantalla:
                self.direccion_marciano = -1
                self.marciano_mueveAbajo(3)
            elif marciano.rect.left <= 0:
                self.direccion_marciano=1
                self.marciano_mueveAbajo(3)
    def marciano_mueveAbajo (self,distancia):
        if self.marcianos:
            for marciano in self.marcianos.sprites():
                marciano.rect.y += distancia
    def marciano_disparo(self):
        if self.marcianos.sprites():
            random_marciano=choice(self.marcianos.sprites())
            sprite_laser = Laser(random_marciano.rect.center,3 ,altura_pantalla)
            self.marciano_lasers.add(sprite_laser)
            print('HOla')
    def extraNave_tiempo(self):
        self.extraNave_spawn -=1
        if self.extraNave_spawn <= 0:
            self.extraNave.add(NaveEnemiga(['right','left'],ancho_pantalla))
    def run(self):
        self.jugador.update()
        self.marcianos.update(self.direccion_marciano)
        self.posicion_marcianos()
        self.extraNave_tiempo()
        self.extraNave.update()

        self.marciano_lasers.update()

        self.jugador.sprite.lasers.draw(pantalla)

        self.jugador.draw(pantalla)
        self.marcianos.draw(pantalla)
        self.marciano_lasers.draw(pantalla)
        self.extraNave.draw(pantalla)


if __name__ == '__main__':
    pygame.init()
    ancho_pantalla = 1200
    altura_pantalla = 800

    pantalla = pygame.display.set_mode((ancho_pantalla, altura_pantalla))
    clock = pygame.time.Clock()
    juego=Juego()
    BackGround = Background('resources/fUG2oM.jpg', [0, 0])


    marcianolaser = pygame.USEREVENT +1
    pygame.time.set_timer(marcianolaser,800)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type ==marcianolaser:
                juego.marciano_disparo()

        pantalla.fill([30,30,30])
        pantalla.blit(BackGround.image, BackGround.rect)
        juego.run()

        pygame.display.flip()
        clock.tick(60)
