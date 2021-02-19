import pygame
from doodler import Doodler
from screen import Screen

class DoodleJumpGame:
    def __init__(self):
        pygame.init()

        self.screen  = Screen()
        self.clock   = pygame.time.Clock()
        self.doodler = Doodler(Screen.WIDTH/2, Screen.HEIGHT/2)
    
    def key_pressed(self, key):
        if key[pygame.K_RIGHT] or key[pygame.K_LEFT]:
            self.doodler.key_pressed(key)
    
    def run(self):
        while True:
            self.clock.tick(30)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                
                if event.type == pygame.KEYDOWN:   # pressinou e soltou a tecla
                    self.doodler.key_pressed(pygame.key.get_pressed())
                
            self.key_pressed(pygame.key.get_pressed())   # manteve a tecla pressionada
            self.screen.draw_background()
            self.screen.draw_sprites(self.doodler.image, self.doodler.rect)

            self.doodler.update()
            self.screen.update()
            

def main():
    game = DoodleJumpGame()
    game.run()

if __name__ == "__main__":
    main()
    
