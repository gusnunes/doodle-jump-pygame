# Classe que implementa o jogador(personagem Doodler)
import pygame

class Doodler(pygame.sprite.Sprite):
    SPEED = 10   # controlar velocidade dos movimentos

    def __init__(self, coord_x, coord_y):
        pygame.sprite.Sprite.__init__(self)
        
        self.image   = pygame.image.load("images/doodler_r.png")
        self.rect    = self.image.get_rect(topleft=(coord_x,coord_y)) # coordenada inicial
        self.speed   = 0
        self.is_jump = False

    # controla o movimento do jogador
    def key_pressed(self,key):
        if key[pygame.K_UP]:
            self.rect[1] -= 10

        elif key[pygame.K_LEFT]:
            self.image   = pygame.image.load("images/doodler_l.png")
            self.rect[0] -= 10

        elif key[pygame.K_RIGHT]:
            self.image   = pygame.image.load("images/doodler_r.png")
            self.rect[0] += 10
    
    def update(self):
        pass