# Classe que implementa a plataforma onde o Doodler pula sobre
import pygame

class Platform(pygame.sprite.Sprite):
    def __init__(self, coord_x, coord_y):
        pygame.sprite.Sprite.__init__(self)
        self.images = [
            pygame.image.load("images/platform_green.png").convert_alpha()
        ]

        self.image = self.images[0]   # primeira plataforma de teste (somente a verde)
        self.rect = self.image.get_rect(center=(coord_x,coord_y))
        self.mask = pygame.mask.from_surface(self.image)
    
    def update():
        pass