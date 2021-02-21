# Classe que implementa o jogador(personagem Doodler)
import pygame

class Doodler(pygame.sprite.Sprite):
    SPEED = 5   # controlar velocidade dos movimentos
    GRAVITY = 0.8   # controlar o pulo do jogador

    def __init__(self, coord_x, coord_y):
        pygame.sprite.Sprite.__init__(self)

        self.images = [   # todas as imagens do Doodler
            pygame.image.load("images/doodler_l.png").convert_alpha(),
            pygame.image.load("images/doodler_r.png").convert_alpha()
        ]

        self.image = self.images[0]   # imagem atual do Doodler

        # hitbox = cria um retangulo do tamanho da imagem (para usar coordenadas)
        self.rect = self.image.get_rect(center=(coord_x,coord_y)) 

    def shoot(self):
        pass

    # controla o movimento do jogador
    def left_movement(self):
        self.image = self.images[0]
        self.rect.x -= Doodler.SPEED

    def right_movement(self):
        self.image = self.images[1]
        self.rect.x += Doodler.SPEED
    
    def update(self):
        pass
