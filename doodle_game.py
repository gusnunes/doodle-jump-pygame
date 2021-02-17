import pygame
from Doodler import Doodler

class DoodleJumpGame:
    def __init__(self, width, height):
        pygame.init()
        pygame.display.set_caption("Doodle Jump")

        self.width   = width
        self.height  = height
        self.screen  = pygame.display.set_mode((width,height))
        self.clock   = pygame.time.Clock()
        self.doodler = Doodler() 
    
    def run(self):
        self.clock.tick(8)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            
            if event.type == pygame.KEYDOWN:
                self.doodler.key_pressed(pygame.key.get_pressed())
        
        pygame.display.update()

def main():
    # definindo tamanho da tela
    WIDTH = 640
    HEIGH = 480

    game = DoodleJumpGame(WIDTH,HEIGH)
    game.run()

if __name__ == "__main__":
    main()
    
