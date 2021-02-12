import pygame

class DoodleJumpGame:
    # definindo cores
    WHITE = 255, 255, 255
    RED   = 255, 0, 0
    BLACK = 0, 0, 0

    def __init__(self, width, height):
        self.width  = width
        self.height = height
        pygame.init()
        pygame.display.set_caption("Doodle Jump")
        self.screen = pygame.display.set_mode((width,height))   

def main():
    # definindo tamanho da tela
    WIDTH = 640
    HEIGH = 480

    DoodleJumpGame(WIDTH,HEIGH)

if __name__ == "__main__":
    main()
    
