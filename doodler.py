# Classe que implementa o jogador(personagem Doodler)
import pygame

class Doodler(pygame.sprite.Sprite):
    # fisica relacionada aos movimentos
    SPEED = 5

    def __init__(self, coord_x, coord_y):
        pygame.sprite.Sprite.__init__(self)

        self.images = [   # todas as imagens do Doodler
            pygame.image.load("images/doodler_l.png").convert_alpha(),
            pygame.image.load("images/doodler_r.png").convert_alpha()
        ]

        self.image = self.images[0]   # imagem atual do Doodler

        # hitbox = retangulo do tamanho da imagem (para usar coordenadas)
        self.rect = self.image.get_rect(center=(coord_x,coord_y)) 

        # mascara usada para detectar colisao
        self.mask = pygame.mask.from_surface(self.image)

        # movimento do jogador (posicao onde se encontra)
        self.pos_x = coord_x
        self.pos_y = coord_y

    def shoot(self):
        pass

    def left_movement(self):
        self.image = self.images[0]
        self.pos_x -= Doodler.SPEED 

    def right_movement(self):
        self.image = self.images[1]
        self.pos_x += Doodler.SPEED
    
    def update(self):
        self.pos_y += Doodler.SPEED
        self.rect.center = (self.pos_x, self.pos_y)
