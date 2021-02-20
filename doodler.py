# Classe que implementa o jogador(personagem Doodler)
import pygame

class Doodler(pygame.sprite.Sprite):
    SPEED = 10   # controlar velocidade dos movimentos

    def __init__(self, coord_x, coord_y):
        pygame.sprite.Sprite.__init__(self)
        
        self.image = pygame.image.load("images/doodler_r.png")
        self.rect  = self.image.get_rect(topleft=(coord_x,coord_y)) # coordenada inicial

    def shoot(self):
        pass

    # controla o movimento do jogador
    def left_movement(self):
        self.image = pygame.image.load("images/doodler_l.png")
        self.rect[0] -= 5

    def right_movement(self):
        self.image = pygame.image.load("images/doodler_r.png")
        self.rect[0] += 5
    
    def update(self):
        pass
