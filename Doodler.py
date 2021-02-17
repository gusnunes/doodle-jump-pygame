# Classe que implementa o jogador(personagem Doodler)
import pygame

class Doodler(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("images/doodler.png")
    
    # controla o movimento do jogador
    def key_pressed(key):
        if key[pygame.K_UP]:
            pass
        
        elif key[pygame.K_LEFT]:
            pass

        elif key[pygame.K_RIGHT]:
            pass

