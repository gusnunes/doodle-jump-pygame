# Classe responsavel por controlar o que aparece na tela
import pygame

class Screen:
    WIDTH  = 320
    HEIGHT = 512

    def __init__(self):
        pygame.display.set_caption("Doodle Jump")
        self.screen = pygame.display.set_mode((Screen.WIDTH,Screen.HEIGHT))
        self.background = pygame.image.load("images/background.png")
    
    def draw_background(self):
        self.screen.blit(self.background, (0, 0))
    
    def draw_doodler(self, image, rect):
        self.screen.blit(image,rect)
    
    def update(self):
        pygame.display.update()
