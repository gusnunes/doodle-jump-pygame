import pygame

class DoodleJumpGame:
    def __init__(self, width, height):
        pygame.init()
        pygame.display.set_caption("Doodle Jump")

        self.width  = width
        self.height = height
        self.screen = pygame.display.set_mode((width,height))
        self.clock  = pygame.time.Clock() 
    
    def run(self):
        pass

def main():
    # definindo tamanho da tela
    WIDTH = 640
    HEIGH = 480

    game = DoodleJumpGame(WIDTH,HEIGH)
    game.run()

if __name__ == "__main__":
    main()
    
