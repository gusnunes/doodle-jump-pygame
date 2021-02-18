import pygame
from doodler import Doodler
from screen import Screen

class DoodleJumpGame:
    def __init__(self):
        pygame.init()

        self.screen  = Screen()
        self.clock   = pygame.time.Clock()
        self.doodler = Doodler() 
    
    def run(self):
        while True:
            self.clock.tick(8)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                
                if event.type == pygame.KEYDOWN:
                    self.doodler.key_pressed(pygame.key.get_pressed())
            
            self.screen.draw_background()
            self.screen.update()
            

def main():
    game = DoodleJumpGame()
    game.run()

if __name__ == "__main__":
    main()
    
