# Classe responsavel por controlar o que aparece na tela
import pygame

class Screen:
    WIDTH  = 320
    HEIGHT = 512

    def __init__(self):
        pygame.display.set_caption("Doodle Jump")

        self.background = pygame.image.load("images/background.png")
        self.screen     = pygame.display.set_mode((Screen.WIDTH,Screen.HEIGHT))
    
    def draw_background(self):
        self.screen.blit(self.background, (0, 0))
    
    def update(self):
        pygame.display.update()
